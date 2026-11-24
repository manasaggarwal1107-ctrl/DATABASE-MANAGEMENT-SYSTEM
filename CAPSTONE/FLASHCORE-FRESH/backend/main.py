from fastapi import FastAPI
from sqlalchemy import text

from app.core.database import DATABASE_URL, engine
from app.routes.admin import router as admin_router
from app.routes.auth import router as auth_router
from app.routes.rossmann import router as rossmann_router
from app.routes.simulation import router as simulation_router
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="FLASHCORE",
    description=(
        "Retail analytics and high-concurrency "
        "inventory simulation platform powered by "
        "authentic Rossmann historical store data."
    ),
    version="1.0.0",
)

# Restrict browser access to explicitly approved frontend origins.
# Locally defaults to Vite; production origins are supplied by the environment.
frontend_origins = os.getenv("FRONTEND_ORIGIN", "http://localhost:5173")
allowed_origins = [
    origin.strip().rstrip("/")
    for origin in frontend_origins.split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=False,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type", "Accept", "Idempotency-Key"],
)

app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(rossmann_router)
app.include_router(simulation_router)


@app.get("/")
def root():
    return {
        "project": "FLASHCORE",
        "database": DATABASE_URL.database,
        "status": "running",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/health/database")
def database_health():
    with engine.connect() as connection:
        actual_database = connection.execute(
            text("SELECT current_database()")
        ).scalar_one()

    return {
        "database": actual_database,
        "status": "connected",
    }

