# Salon & Beauty Parlour Management System (SBPMS)

Built on Frappe Framework v15+ and ERPNext v15+.

## Features
- **Appointment & Booking**: Online/offline booking, slot engine, stylist auto-assignment.
- **Salon Services**: Session tracking, before/after photos, treatment checklists.
- **Membership & Loyalty**: Loyalty points, prepaid wallet, subscription plans.
- **Inventory Management**: Auto stock deduction, chemical consumption logs, expiry alerts.
- **Customer Portal**: Self-booking, membership dashboard, invoice download.
- **Reports & Analytics**: Stylist productivity, revenue analysis, retention dashboard.

## Installation
1. Get the app: `bench get-app salon_management`
2. Install the app: `bench --site [your-site] install-app salon_management`
3. Migrate: `bench --site [your-site] migrate`

## Naming Series
- APPT, SESS, MEM, LTXN, WLET, PUSG, SASS, FDBK, PNOT, SBAT

## Core Modules
1. appointment_booking
2. salon_services
3. membership_loyalty
4. inventory_management
5. customer_portal
6. reports_analytics
