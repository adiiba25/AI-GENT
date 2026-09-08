# ArgeoDatum Agent

ArgeoDatum Agent is the internal business operating system and AI assistant for Argeo Datum Business World LLP.

## Goal
Build one system that connects client management, quotations, project operations, UAV/GIS workflows, finance, equipment, reporting, and AI-assisted decision support.

## Version 1 modules
1. CRM / Clients
2. Quotations
3. Project Management
4. Finance / Invoices / Payments
5. UAV & Equipment
6. AI Assistant

## Core workflow
Client Inquiry → Opportunity → Quotation → Accepted Quote → Project → Team & Equipment Assignment → Fieldwork → Processing → QA/QC → Deliverables → Invoice → Payment → Close Project

## Management dashboard
The home dashboard should show:
- Active projects
- Projects awaiting payment
- Total quoted value
- Revenue received
- Outstanding invoices
- Monthly expenses
- Profit by project
- Equipment availability
- Upcoming deadlines
- Clients requiring follow-up

## AI assistant examples
- Which clients owe us money?
- How much profit did we make from UAV projects this quarter?
- Prepare a quotation for a 25 km² LiDAR survey using M400 + L2.
- What equipment is available next week?
- Generate the weekly project progress report.
- Which quotations have not received a response in the last 7 days?
- Draft a follow-up message to the client.

## Recommended implementation approach
Start with a reliable database and workflow engine first. Add AI only after the business data model and permissions are stable.

Suggested stack for the MVP:
- Frontend: Next.js / React
- Backend/API: FastAPI or Next.js server routes
- Database: PostgreSQL
- ORM: SQLAlchemy or Prisma
- Authentication: role-based access control
- AI: OpenAI API with tool/function calling against approved backend actions
- File storage: local/S3-compatible storage initially, later SharePoint/Google Drive if required
- Maps/GIS: PostGIS + MapLibre/Leaflet for project footprints and survey locations

## Start here
Read `AGENTS.md`, then `docs/ARCHITECTURE.md`, `docs/DATABASE.md`, and `docs/ROADMAP.md` before implementing features.
