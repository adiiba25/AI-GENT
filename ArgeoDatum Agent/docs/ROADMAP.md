# Roadmap

## Phase 1 — Foundation
- Project structure and Docker development environment
- PostgreSQL/PostGIS
- Authentication and RBAC
- Organization/users
- Audit logging foundation

## Phase 2 — CRM & Sales
- Clients and contacts
- Opportunities pipeline
- Follow-up dates
- Quotations and line items
- Quote status/versioning
- Convert accepted quotation into project

## Phase 3 — Projects & UAV/GIS Operations
- Project register
- Milestones and staff assignments
- Survey operation records
- GCP/SCP/control point tracking
- Processing status and QA/QC
- Deliverables register
- Map project AOIs and locations

## Phase 4 — Finance
- Expenses by project
- Invoices and invoice items
- Payments
- Outstanding receivables
- Project profitability
- Financial dashboard

## Phase 5 — Equipment
- Asset register
- Availability calendar
- Project assignments
- Maintenance records
- Conflict warnings when equipment is double-booked

## Phase 6 — Management Dashboard
- Active projects
- Sales pipeline
- Quoted value
- Revenue received
- Outstanding invoices
- Monthly expenses
- Profit by project
- Upcoming deadlines
- Equipment availability
- Follow-up queue

## Phase 7 — AI Assistant
Start read-only with approved tools:
- business overview
- overdue invoice summary
- project status summary
- equipment availability
- quotation follow-up list
- weekly/monthly management report

Then add draft-generation tools:
- quotation draft
- invoice reminder
- client email/WhatsApp follow-up draft
- project progress report

Only later add confirmed write actions.

## MVP definition of done
A director can log in and:
1. Register a client.
2. Create an opportunity.
3. Generate and approve a quotation.
4. Convert it to a project.
5. Assign a team and equipment.
6. Track fieldwork/processing/deliverables.
7. Record project expenses.
8. Issue an invoice and record payment.
9. See profit/outstanding balances on a dashboard.
10. Ask the AI assistant questions about these records.

## First Codex task
Create the initial monorepo application under `ArgeoDatum Agent/` with:
- `apps/web` — Next.js frontend
- `apps/api` — FastAPI backend
- `docker-compose.yml`
- PostgreSQL/PostGIS service
- SQLAlchemy/Alembic setup
- health endpoint
- initial models for organizations, users, clients, opportunities, quotations, projects, equipment, invoices, payments and expenses
- seed script with demo Argeo Datum data
- README startup commands

Do not implement external messaging or autonomous financial actions in the first milestone.
