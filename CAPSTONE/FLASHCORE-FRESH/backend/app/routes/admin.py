from datetime import datetime, timezone
from typing import Literal

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, ConfigDict
from sqlalchemy import select, update
from sqlalchemy.orm import Session

from app.core.auth_dependencies import get_current_user, require_roles
from app.core.database import get_db
from app.models.auth import AuthSession, User


router = APIRouter(
    prefix="/api/admin",
    tags=["Administration"],
    dependencies=[Depends(require_roles("admin"))],
)


class AdminUserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: str
    role: str
    status: str
    created_at: datetime


class RoleUpdate(BaseModel):
    role: Literal["admin", "analyst", "operator"]


class StatusUpdate(BaseModel):
    status: Literal["active", "disabled"]


def lock_active_admins(db: Session) -> list[User]:
    return list(
        db.scalars(
            select(User)
            .where(User.role == "admin", User.status == "active")
            .order_by(User.id)
            .with_for_update()
        ).all()
    )


def revoke_user_sessions(db: Session, user_id: int) -> None:
    db.execute(
        update(AuthSession)
        .where(
            AuthSession.user_id == user_id,
            AuthSession.revoked_at.is_(None),
        )
        .values(revoked_at=datetime.now(timezone.utc))
    )


@router.get("/users", response_model=list[AdminUserResponse])
def list_users(db: Session = Depends(get_db)):
    return db.scalars(
        select(User).order_by(User.id)
    ).all()


@router.patch(
    "/users/{user_id}/role",
    response_model=AdminUserResponse,
)
def update_user_role(
    user_id: int,
    payload: RoleUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    user = db.get(User, user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found.")

    if user.id == current_user.id:
        raise HTTPException(
            status_code=409,
            detail="You cannot change your own role.",
        )

    if user.role == payload.role:
        return user

    if user.role == "admin" and user.status == "active":
        active_admins = lock_active_admins(db)

        if len(active_admins) <= 1:
            raise HTTPException(
                status_code=409,
                detail="Cannot demote the last active administrator.",
            )

    user.role = payload.role
    user.updated_at = datetime.now(timezone.utc)

    revoke_user_sessions(db, user.id)

    db.commit()
    db.refresh(user)

    return user


@router.patch(
    "/users/{user_id}/status",
    response_model=AdminUserResponse,
)
def update_user_status(
    user_id: int,
    payload: StatusUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    user = db.get(User, user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found.")

    if user.id == current_user.id:
        raise HTTPException(
            status_code=409,
            detail="You cannot change your own account status.",
        )

    if user.status == payload.status:
        return user

    if (
        user.role == "admin"
        and user.status == "active"
        and payload.status == "disabled"
    ):
        active_admins = lock_active_admins(db)

        if len(active_admins) <= 1:
            raise HTTPException(
                status_code=409,
                detail="Cannot disable the last active administrator.",
            )

    user.status = payload.status
    user.updated_at = datetime.now(timezone.utc)

    if payload.status == "disabled":
        revoke_user_sessions(db, user.id)

    db.commit()
    db.refresh(user)

    return user
