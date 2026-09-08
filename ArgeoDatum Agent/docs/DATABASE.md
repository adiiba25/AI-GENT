# Database Blueprint

## Conventions
- UUID primary keys
- created_at / updated_at timestamps
- created_by where useful
- NUMERIC/Decimal for money
- ISO currency codes
- status enums validated at application layer

## Identity
### organizations
- id
- name
- legal_name
- currency
- timezone

### users
- id
- organization_id
- name
- email
- role
- active

## CRM
### clients
- id
- organization_id
- client_type
- company_name
- contact_name
- email
- phone
- country
- address
- notes
- status

### contacts
- id
- client_id
- name
- title
- email
- phone
- primary_contact

### opportunities
- id
- client_id
- title
- service_type
- description
- estimated_value
- currency
- probability
- stage
- expected_close_date
- next_follow_up_at
- owner_id

### interactions
- id
- client_id
- opportunity_id
- interaction_type
- occurred_at
- summary
- next_action

## Quotations
### quotations
- id
- quote_number
- client_id
- opportunity_id
- version
- issue_date
- valid_until
- currency
- subtotal
- tax_amount
- discount_amount
- total
- status
- terms
- prepared_by
- approved_by

### quotation_items
- id
- quotation_id
- description
- service_code
- quantity
- unit
- unit_price
- line_total
- sort_order

## Projects
### projects
- id
- project_code
- client_id
- quotation_id
- name
- service_type
- description
- country
- location_name
- geometry
- start_date
- target_end_date
- actual_end_date
- status
- contract_value
- currency
- project_manager_id

### project_milestones
- id
- project_id
- name
- due_date
- completed_at
- status

### project_assignments
- id
- project_id
- user_id
- role_on_project
- start_date
- end_date

### project_deliverables
- id
- project_id
- deliverable_type
- name
- status
- file_url
- submitted_at
- accepted_at
- notes

## UAV / GIS Operations
### survey_operations
- id
- project_id
- operation_type
- survey_area_km2
- corridor_length_km
- methodology
- flight_start
- flight_end
- processing_status
- qaqc_status
- notes

### control_points
- id
- project_id
- point_code
- point_type
- easting
- northing
- elevation
- coordinate_system
- observed_at
- quality_status

### processing_jobs
- id
- project_id
- operation_id
- processing_type
- software
- started_at
- completed_at
- status
- output_location
- notes

## Equipment
### equipment
- id
- asset_code
- name
- category
- manufacturer
- model
- serial_number
- purchase_date
- status
- current_location
- notes

### equipment_assignments
- id
- equipment_id
- project_id
- assigned_from
- assigned_to
- assigned_by
- status

### maintenance_records
- id
- equipment_id
- maintenance_type
- performed_at
- next_due_at
- cost
- currency
- notes

## Finance
### expenses
- id
- project_id
- category
- description
- vendor
- expense_date
- amount
- currency
- payment_method
- receipt_url
- status
- entered_by

### invoices
- id
- invoice_number
- client_id
- project_id
- issue_date
- due_date
- currency
- subtotal
- tax_amount
- total
- amount_paid
- balance_due
- status

### invoice_items
- id
- invoice_id
- description
- quantity
- unit_price
- line_total

### payments
- id
- invoice_id
- payment_date
- amount
- currency
- payment_method
- reference
- notes

## Audit
### audit_logs
- id
- user_id
- action
- entity_type
- entity_id
- before_json
- after_json
- created_at

## Key relationships
Client → Opportunities → Quotations → Projects → Invoices → Payments

Project → Assignments / Survey Operations / Deliverables / Expenses / Equipment Assignments

Equipment → Equipment Assignments / Maintenance Records
