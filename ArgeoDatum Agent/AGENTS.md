# AGENTS.md — ArgeoDatum Agent

## Mission
Build a practical internal business operating system and AI assistant for Argeo Datum Business World LLP.

## Product principles
- Business workflow first, AI second.
- Keep finance, quotations, projects, equipment and deliverables auditable.
- Never let AI directly perform destructive or financial actions without explicit user confirmation.
- Prefer simple, maintainable architecture over unnecessary agent complexity.
- GIS/UAV operations are first-class domain objects, not generic project notes.

## MVP scope
1. CRM / clients / contacts / opportunities
2. Quotations and quotation line items
3. Projects and project milestones
4. UAV/GIS operational records
5. Equipment and assignment calendar
6. Expenses, invoices, payments and receivables
7. Management dashboard
8. AI assistant with read-only business Q&A first, then approved actions

## Primary workflow
Client Inquiry → Opportunity → Quotation → Accepted → Project → Assignment → Fieldwork → Processing → QA/QC → Delivery → Invoice → Payment → Project Close

## Suggested architecture
- PostgreSQL + PostGIS
- Next.js/React frontend
- FastAPI backend (preferred) or Next.js API routes
- SQLAlchemy + Alembic if FastAPI is used
- REST API first; add async jobs only when needed
- OpenAI tool calling through a backend service layer

## Roles
- Admin / Director
- Finance
- Project Manager
- Survey/UAV Operations
- GIS/Processing
- Viewer/Auditor

## AI safety model
AI may:
- search and summarize internal records
- prepare draft quotations
- draft client follow-ups
- generate management/project reports
- detect overdue invoices, projects or quotations

AI must require confirmation before:
- sending external messages
- issuing/finalizing quotations
- marking invoices as paid
- deleting records
- changing project financial values
- closing projects

## Coding expectations
- Use typed models and validation.
- Add migrations for every schema change.
- Keep secrets in environment variables.
- Write tests around calculations, permissions, quotation totals and financial posting logic.
- Keep domain logic out of UI components.
- Use UUIDs for primary keys unless there is a strong reason not to.
- Store monetary values using NUMERIC/Decimal, never floats.
- Track created_at, updated_at, created_by where meaningful.

## First implementation milestone
Build authentication, organizations/users, clients, opportunities, quotations, projects, invoices, payments and equipment tables plus a minimal dashboard and seeded demo data.

Before coding, read the files in `docs/`.
