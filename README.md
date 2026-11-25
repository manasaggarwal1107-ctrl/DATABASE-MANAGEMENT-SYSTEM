# FLASHCORE

**Retail Analytics & Flash-Sale Simulation Platform** — DBMS Capstone Project, K.R. Mangalam University.

FLASHCORE is a full-stack retail analytics and flash-sale simulation application built around the Rossmann Store Sales dataset. It combines historical retail analytics with a transactional simulation environment to demonstrate relational database design, SQL operations, database integrity, transaction management, concurrency control and backend integration.

The project uses PostgreSQL as its central data layer, with a React frontend and FastAPI backend.

## Technology Stack

| **Layer** | **Technology** | **Purpose** |
|---|---|---|
| Frontend | React 19 | Interactive application interface |
| Frontend language | TypeScript | Typed frontend development |
| Build tool | Vite | Frontend development and build |
| Backend | Python + FastAPI | REST API and application logic |
| ORM | SQLAlchemy 2 | Relational database interaction |
| Database driver | Psycopg 3 | PostgreSQL connectivity |
| Database | PostgreSQL | Persistent relational storage |
| API | REST | Frontend-backend communication |

## Quick access

- **Live Application:** [https://flashcore-psi.vercel.app](https://flashcore-psi.vercel.app)
- **Backend Service:** [https://database-management-system-s1g5.onrender.com](https://database-management-system-s1g5.onrender.com)
- **Repository:** [DATABASE-MANAGEMENT-SYSTEM](https://github.com/manasaggarwal1107-ctrl/DATABASE-MANAGEMENT-SYSTEM)

## What is implemented

FLASHCORE is organized around two distinct database workloads.

| **Workload** | **Purpose** | **Primary Data Domain** |
|---|---|---|
| Historical Retail Analytics (OLAP) | Analyse historical retail sales and store performance | Rossmann historical dataset |
| Flash-Sale Simulation (OLTP) | Model transactional flash-sale and inventory operations | Simulation-generated activity |

### Historical Retail Analytics

- Store information management.
- Historical daily sales records.
- Dataset import tracking.
- Dataset import error tracking.
- Store-level retail analytics.

### Flash-Sale Simulation

- Simulation run management.
- Simulation product management.
- Inventory management.
- Flash-sale configuration.
- Flash-sale product association.
- Purchase attempt tracking.
- Transaction logging.

### User and Activity Management

- User records.
- Authentication session records.
- Audit logging.

The frontend also provides analytical views such as Orders and Customers. These are not standalone tables in the reported active database schema.

## Database Architecture

The application follows a layered client-server architecture:

```text
                 USER
                   |
                   v
           REACT FRONTEND
          React + TypeScript
                   |
                   v
                REST API
                   |
                   v
            FASTAPI BACKEND
                   |
                   v
              SQLAlchemy 2
                   |
                   v
                Psycopg 3
                   |
                   v
              POSTGRESQL
               DATABASE
```

The frontend never connects directly to PostgreSQL. Database access is mediated through the backend API.

## Database Schema

The final database verification audit reported **14 active relational tables**.

| **No.** | **Table** | **Purpose** |
|---:|---|---|
| 1 | `users` | User records |
| 2 | `auth_sessions` | Authentication session records |
| 3 | `stores` | Retail store information |
| 4 | `daily_store_sales` | Historical daily sales records |
| 5 | `dataset_imports` | Dataset import tracking |
| 6 | `dataset_import_errors` | Dataset import error tracking |
| 7 | `audit_logs` | Audit records |
| 8 | `simulation_runs` | Simulation execution records |
| 9 | `simulation_products` | Simulation product records |
| 10 | `simulation_inventory` | Inventory records |
| 11 | `flash_sales` | Flash-sale configurations |
| 12 | `flash_sale_products` | Flash-sale product associations |
| 13 | `purchase_attempts` | Purchase attempt records |
| 14 | `transactions_log` | Transaction records |

### Reported Database Statistics

| **Metric** | **Count** |
|---|---:|
| Active relational tables | 14 |
| Constraints | 130 |
| Foreign keys | 14 |
| Indexes | 28 |

These figures are based on the final database verification report.

Historical Rossmann records and synthetic simulation activity are maintained as separate data domains.

## DBMS Concepts Demonstrated

| **Concept** | **Implementation** |
|---|---|
| Relational modelling | Structured relational schema |
| Normalization | Normalized relational design |
| Primary keys | Entity identification |
| Foreign keys | Referential integrity |
| Constraints | Database-level integrity enforcement |
| Indexing | 28 reported indexes |
| CRUD | Database-backed application operations |
| SQL | Queries, joins, aggregations and data manipulation |
| ACID | Transaction-oriented database operations |
| Concurrency control | Explicit row-level locking |
| Transaction isolation | PostgreSQL READ COMMITTED |
| Idempotency | Duplicate operation protection |
| Audit logging | Activity and transaction records |

## Transaction Management and Concurrency

FLASHCORE implements transaction-oriented inventory management.

The reported implementation uses:

- PostgreSQL `READ COMMITTED` isolation.
- Explicit `SELECT FOR UPDATE` row locking.
- Conditional stock updates.
- Idempotency protections.
- Transaction-based stock and ledger operations.

These mechanisms are intended to protect transactional consistency during simultaneous operations.

### Reported Concurrency Verification

| **Scenario** | **Concurrent Operations** | **Reported Result** |
|---|---:|---|
| Inventory allocation | 50 threads | 10 successful allocations, 40 rejected |
| Idempotency | 20 identical requests | 1 operation, 19 duplicate replays |
| Stock adjustments | 20 concurrent adjustments | Final stock exactly 30 |
| Purchase attempts | 10 threads | 1 successful purchase, 9 rejected |
| Multiple products | 30 threads | 30 successful, zero deadlocks |

These results describe the scenarios documented in the final verification evidence. They should not be interpreted as a guarantee for larger or arbitrary concurrency levels.

## Testing and Verification

A final database verification exercise was conducted covering production connectivity, application testing, selected transactional scenarios and backup/recovery checks.

### Reported Results

| **Area** | **Result** |
|---|---|
| Production database connectivity | Reported successful |
| `/health/database` | HTTP 200 |
| `/api/health/database` | HTTP 200 |
| Frontend automated tests | 124/124 reported passing |
| Backend test catalogue | 144 tests catalogued; fresh execution of all 144 not established |
| Concurrency verification | Selected scenarios documented |
| Backup and restore | Reported successful in isolated test databases |
| Selected-table data parity | Reported |

The backend test catalogue must not be interpreted as 144 freshly executed passing tests.

## What was and was not verified

The final verification exercise identified the following limitations:

- The local PostgreSQL service was stopped during the final audit, blocking local mutation tests.
- Empirical query execution plan and latency evidence remains incomplete.
- Complete end-to-end verification of every frontend-to-database operation has not been established.
- Nine frontend dependency advisories remained unresolved: 2 Critical, 2 High and 5 Moderate.
- The exact managed PostgreSQL provider and server version remain unverified.
- Backup and restore verification was performed in isolated test databases, not as a production disaster-recovery guarantee.

These limitations are retained to distinguish verified results from areas that have not been fully established.

## Live Deployment

| **Service** | **Deployment** |
|---|---|
| Frontend | [Vercel Application](https://flashcore-psi.vercel.app) |
| Backend | [Render Service](https://database-management-system-s1g5.onrender.com) |
| Source Code | [GitHub Repository](https://github.com/manasaggarwal1107-ctrl/DATABASE-MANAGEMENT-SYSTEM) |

Production database connectivity was reported successful during the final verification audit.

The exact managed PostgreSQL provider and version have not been independently established in that audit.

## Local Development

### Prerequisites

- Python compatible with the backend dependencies.
- Node.js and npm.
- PostgreSQL.
- Git.

### Clone the Repository

```bash
git clone https://github.com/manasaggarwal1107-ctrl/DATABASE-MANAGEMENT-SYSTEM.git
cd DATABASE-MANAGEMENT-SYSTEM
```

### Backend Setup

Navigate to the backend directory containing the project's dependency file.

Create a virtual environment:

```bash
python -m venv venv
```

Activate on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure the required database credentials and environment variables using the repository's existing configuration instructions.

Start the backend using its configured FastAPI entry point.

### Frontend Setup

Navigate to the frontend directory containing `package.json`.

Install dependencies:

```bash
npm install
```

Start the development server using the configured Vite script:

```bash
npm run dev
```

**Note:** Exact directory names, entry points, environment variable names and database initialization commands should be taken from the current repository configuration. They are intentionally not assumed here.

## Project Documentation

The repository includes a dedicated technical documentation portfolio.

| **Documentation** | **Purpose** |
|---|---|
| `FLASHCORE-FINAL-DATABASE-VERIFICATION-REPORT.md` | Final database verification findings |
| `FLASHCORE-DBMS-DEMONSTRATION-GUIDE.md` | Practical demonstration guide |
| `schema_inventory.json` | Database schema inventory |
| `frontend_backend_traceability.json` | Frontend-backend traceability evidence |
| `acid_concurrency_summary.json` | ACID and concurrency verification summary |

The documentation portfolio also includes reports, diagrams, screenshots and supporting implementation material.

Refer to `CAPSTONE/FLASHCORE-FRESH/docs/OFFICIAL DOCUMENTATION/` for the published documentation collection.

## Folder Structure

The following is a conceptual overview of the project organization:

```text
DATABASE-MANAGEMENT-SYSTEM/
|
|-- CAPSTONE/
|   |
|   |-- FLASHCORE-FRESH/
|       |
|       |-- backend/
|       |   |-- app/
|       |   |-- tests/
|       |   |
|       |-- frontend/
|       |
|       |-- docs/
|       |   |-- OFFICIAL DOCUMENTATION/
|       |
|       |-- artifacts/
|           |-- FLASHCORE-FINAL-DATABASE-VERIFICATION-REPORT.md
|           |-- FLASHCORE-DBMS-DEMONSTRATION-GUIDE.md
|
|-- README.md
```

This is a high-level representation; refer to the actual repository for the complete directory structure.

## Academic Context

| **Field** | **Details** |
|---|---|
| Project | FLASHCORE |
| Category | DBMS Capstone Project |
| Student | Manas Aggarwal |
| Roll Number | 2501730302 |
| Degree | B.Tech CSE (AI & ML) |
| Semester | Third Semester |
| Section | A |
| Institution | K.R. Mangalam University |
| School | School of Engineering and Technology |
| Academic Session | 2026–2027 |
| Submitted To | Ms. Mansi Kajal, Assistant Professor, SOET |

## Author

**Manas Aggarwal**

B.Tech Computer Science and Engineering  
Artificial Intelligence and Machine Learning  
K.R. Mangalam University

GitHub: [@manasaggarwal1107-ctrl](https://github.com/manasaggarwal1107-ctrl)

---

## Project Objective

FLASHCORE was developed to demonstrate the practical role of database engineering in modern retail applications.

By bringing together historical retail analytics and transactional flash-sale simulation, the project explores the challenges of designing relational data models, enforcing integrity, managing concurrent operations and integrating a database with a full-stack application.

The central focus is not simply storing and retrieving data, but understanding how database architecture, transactions, SQL and concurrency control support a reliable data-driven software system.

---

<p align="center">
  <strong>FLASHCORE</strong><br/>
  Retail Intelligence. Transactional Integrity. Database Engineering.
</p>
