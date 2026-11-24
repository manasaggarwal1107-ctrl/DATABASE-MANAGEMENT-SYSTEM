# FLASHCORE Frontend

> Precision at the speed of demand.

Command-centre frontend for the FLASHCORE flash-sale and inventory engine.
React 18 · Vite · TypeScript (strict) · Tailwind CSS · React Router · TanStack Query · Recharts · Lucide · Framer Motion · React Hook Form + Zod.

## Status

**Phase 1 complete — shell, design system, API layer and all 13 sections are built. Backend integration is pending `API_CONTRACT.md`.**

No endpoint paths have been invented. Every endpoint in `src/services/api/endpoints.ts` is `pending-contract`; pages bound to one show an "Awaiting API contract" state and send no request. No business data, metrics or health statuses are hardcoded anywhere.

This code was authored without being installed, type-checked, linted or test-run (the authoring environment had no package-registry access). **Run the commands below before relying on it** — see `INTEGRATION_HANDOVER.md` § Verification status.

## Quick start

```bash
cd frontend
cp .env.example .env.local
npm install
npm run dev          # http://localhost:5173
```

| Command             | Purpose                                   |
| ------------------- | ----------------------------------------- |
| `npm run dev`       | Vite dev server (proxies `/api` → backend) |
| `npm run build`     | Type-check, then production build         |
| `npm run typecheck` | `tsc --noEmit` (app + node configs)       |
| `npm run lint`      | ESLint                                    |
| `npm test`          | Vitest (run once)                         |
| `npm run test:watch`| Vitest watch mode                         |

## Environment variables

See `.env.example`: `VITE_API_BASE_URL` (default `/api/v1`), `VITE_APP_ENV` (`development`|`production`), `VITE_API_TIMEOUT_MS`, `VITE_DEV_PROXY_TARGET`, `VITE_IDEMPOTENCY_HEADER`.

## Documentation

- `FRONTEND_ARCHITECTURE.md` — structure, data flow, state/error handling
- `DESIGN_SYSTEM.md` — tokens, components, data-origin conventions
- `INTEGRATION_HANDOVER.md` — endpoints expected, integration steps, limitations
- `API_CONTRACT.md` — integration notes and adapter points (the backend's authoritative contract replaces/extends it)
