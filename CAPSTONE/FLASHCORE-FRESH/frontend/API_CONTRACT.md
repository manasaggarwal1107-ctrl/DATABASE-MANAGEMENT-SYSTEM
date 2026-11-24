# API_CONTRACT.md — Frontend integration notes

> **The backend team's `API_CONTRACT.md` has NOT been received.** This file is the frontend's *needs list and adapter map*, not a contract. When the real contract arrives, treat it as authoritative, replace this file with it, and work through the checklist below.

Base URL: `/api/v1` (`VITE_API_BASE_URL`). Transport: JSON over REST; CSV upload via multipart.

## What the frontend needs, per capability

Registry id (in `endpoints.ts`) · method · purpose · UI consumer. All are currently `pending-contract`.

| Registry id | Method | Needed for | Consumer |
| --- | --- | --- | --- |
| overview.summary | GET | KPI metrics (all nullable) | OverviewPage |
| overview.salesSeries | GET | Sales over time (`TimeSeries`) | Overview |
| overview.purchaseOutcomes | GET | Success/failure distribution | Overview |
| overview.inventoryAllocation | GET | Physical vs flash-sale allocation | Overview |
| overview.flashSalePerformance | GET | Per-sale utilisation (`Collection<FlashSale>`) | Overview |
| overview.activity | GET | Recent activity | Overview |
| products.list / get / create / update | GET GET POST PATCH | Catalogue, detail, forms | Products |
| inventory.list / movements / adjust | GET GET POST | Stock, history, adjustment | Inventory |
| flashSales.list / get / create / update | GET GET POST PATCH | Sales CRUD + performance | Flash Sales |
| orders.list / get | GET | Orders + lines | Orders |
| customers.list / get / orders | GET | Customers + history (`:id`) | Customers |
| analytics.salesTrend / orderVolume / conversion / inventoryUtilisation / flashSalePerformance / failureRates | GET | Period charts (`from`,`to`) | Analytics |
| analytics.export | GET | Report export | Analytics |
| transactions.list / get | GET | Purchase attempts | Transaction Monitor |
| concurrency.strategies / start / runs / run | GET POST GET GET | Simulation lab | Concurrency Lab |
| imports.list / get / upload | GET GET POST (multipart) | CSV imports + error report | Data Imports |
| audit.list | GET | Audit entries | Audit Logs |
| system.health | GET | Version, database, services | System Health |

## Questions the contract must answer

1. **Auth** — scheme (Bearer? cookie?), login/refresh endpoints, 401/403 semantics. (`services/api/auth.ts`)
2. **Error format** — body shape and field-level validation errors. (`errors.ts → messageFromBody`)
3. **Pagination** — envelope and parameter names; sort/filter/search parameter names. (`pagination.ts → toQuery / adaptPage`)
4. **Money** — decimal strings? currency per record?
5. **Origin field** — name and values (`real | imported | manual | simulation`) on every resource; confirm simulation data is excluded from business endpoints server-side.
6. **Key casing** — snake_case or camelCase (the client handles both).
7. **Idempotency** — header name, key format, replay response semantics, and whether purchase endpoints are in scope for the frontend at all. (`VITE_IDEMPOTENCY_HEADER`)
8. **Simulation** — documented endpoints, limits (workers / volume), run lifecycle (sync vs polled), strategy list, whether comparison is provided.
9. **Imports** — multipart field names, size limit, status values, error-report shape.
10. **Date/period parameters** for analytics and filters (`from`/`to` assumed).

## Adapter points (the only places that should change)

| File | Change |
| --- | --- |
| `services/api/endpoints.ts` | set `path` + `status: 'confirmed'` per endpoint |
| `services/api/pagination.ts` | list envelope + query param names |
| `services/api/errors.ts` | `messageFromBody` for the real error format |
| `services/api/auth.ts` | auth scheme |
| `types/api.ts` | reconcile every interface with real schemas |
| `features/imports/UploadPanel.tsx` | multipart field names |
| `features/analytics/periods.ts` | period parameter names |
