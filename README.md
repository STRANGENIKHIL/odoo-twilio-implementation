# Odoo - Phone Call Notes Custom Module

This repository contains the solution for the Odoo Developer Internship Technical Assessment. The project implements a custom Odoo module, `phone_call_notes`, to log and track customer phone conversations.

## Live Demo & Deployment

The application is deployed and available live on Railway:
- **Live Deployment Link**: [https://odoo-twilio-implementation-production.up.railway.app](https://odoo-twilio-implementation-production.up.railway.app)

---

## Repository Contents

- [custom_addons/phone_call_notes/](file:///d:/Odoo-Twilio-Intern-Position/custom_addons/phone_call_notes): The Odoo custom addon code.
- [HOW_TO_RUN.md](file:///d:/Odoo-Twilio-Intern-Position/HOW_TO_RUN.md): Step-by-step instructions to run Odoo & PostgreSQL locally.
- [Odoo_Developer_Technical_Assessment.md](file:///d:/Odoo-Twilio-Intern-Position/Odoo_Developer_Technical_Assessment.md): The technical assessment requirements checklist.
- [DESIGN.md](file:///d:/Odoo-Twilio-Intern-Position/DESIGN.md): UI Design and alignment guide.
- [Dockerfile](file:///d:/Odoo-Twilio-Intern-Position/Dockerfile) & [docker-compose.yml](file:///d:/Odoo-Twilio-Intern-Position/docker-compose.yml): Configuration files for containerized local setup and deployment.

---

## Features Implemented

1. **Inline Call Button**: Placed directly next to the phone field on the Contact form.
2. **Interactive Popup Wizard**: Opens on click to capture call status (Pending, Connected, Busy, No Answer) and custom notes.
3. **Smart Button on Contacts**: Displays the live call count and navigates directly to logs for the contact.
4. **Phone Menu & Call Logs View**:
   - **Kanban View**: Visual summary cards of call logs.
   - **Tree (List) View**: Tabular overview.
   - **Form View**: Detailed layout with auto-populated date and current user (Bonus).
   - **Pivot & Graph Views**: Data analysis of status patterns and user logs.
   - **Search View**: Custom filtering and grouping filters.
5. **Security (ACLs)**: Access control constraints ensuring only internal users can view/manage call records.
