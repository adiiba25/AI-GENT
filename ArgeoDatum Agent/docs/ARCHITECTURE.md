# Architecture

## Objective
Create a modular internal operating system for Argeo Datum that can grow from an MVP into a full AI-assisted business platform.

## Core components

### Web application
- Next.js / React
- Responsive dashboard
- Role-aware navigation
- Forms for clients, opportunities, quotations, projects, invoices, expenses and equipment

### Backend API
Preferred: FastAPI.
Responsibilities:
- authentication/authorization
- business rules
- quotation pricing calculations
- project lifecycle transitions
- financial posting
- equipment assignment conflicts
- reporting endpoints
- AI tool endpoints

### Database
PostgreSQL with PostGIS.
Use relational tables for operational and financial data. Use PostGIS geometry for project AOIs, survey locations and asset locations.

### AI service
The AI assistant should not query the database directly. It should call approved backend tools such as:
- search_clients
- list_overdue_invoices
- get_project_summary
- prepare_quotation_draft
- list_available_equipment
- generate_weekly_report

Begin read-only. Add write tools only after permissions and confirmation flows are tested.

### File storage
Use object storage for:
- proposals
- signed quotations
- contracts
- project imagery metadata
- reports
- deliverables
- invoices/receipts

Store file metadata and links in PostgreSQL, not large binaries.

## Domain modules

### CRM
Clients, contacts, leads/opportunities, interactions, follow-ups.

### Sales / Quotations
Quotation header, line items, taxes, discounts, status, expiry and version history.

### Projects
Project metadata, location, AOI, milestones, assignments, progress and deliverables.

### UAV & GIS Operations
Drone, payload, GNSS equipment, survey method, area/length, flight dates, GCP/SCP records, processing status, QA/QC and outputs.

### Finance
Expenses, invoices, payments, receivables, revenue and project profitability.

### Equipment
Asset register, status, maintenance, availability and project assignments.

### Reporting
Management dashboard, project reports, outstanding receivables, quotation pipeline and equipment utilization.

## Suggested API boundaries
- /auth
- /clients
- /opportunities
- /quotations
- /projects
- /operations
- /equipment
- /expenses
- /invoices
- /payments
- /reports
- /ai/tools

## Security
- RBAC at API level
- Audit trail for important financial/project changes
- Soft-delete for business records where appropriate
- Confirmation token/workflow for AI-assisted write actions
- Environment-based secrets
- Database backups

## Initial deployment
Local development with Docker Compose:
- web
- api
- postgres/postgis

Later add managed hosting and object storage.
