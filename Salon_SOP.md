# 📘 Salon & Beauty Parlour Management System — Standard Operating Procedure (SOP)

### Functional Guide for Salon Operations, Customer Experience & Beauty Service Management

---

> **Document Version:** 1.0  
> **Application:** Salon ERP on ERPNext v15  
> **Audience:** Salon Owners, Branch Managers, Receptionists, Stylists, Spa Therapists, Inventory Managers, Accounts Teams, Customer Support Teams  
> **Support:** support@salonbiz.in

---

## 📋 Table of Contents

1. [Getting Started — First Login](#1-getting-started--first-login)
2. [Module 1 — Appointment & Booking Management](#2-module-1--appointment--booking-management)
3. [Module 2 — Salon Services & Treatment Management](#3-module-2--salon-services--treatment-management)
4. [Module 3 — Customer Membership & Loyalty Management](#4-module-3--customer-membership--loyalty-management)
5. [Module 4 — Inventory & Product Usage Management](#5-module-4--inventory--product-usage-management)
6. [Module 5 — Customer Portal & Mobile Experience](#6-module-5--customer-portal--mobile-experience)
7. [Module 6 — Billing & Financial Operations](#7-module-6--billing--financial-operations)
8. [Module 7 — Reports & Analytics](#8-module-7--reports--analytics)
9. [Daily / Weekly / Monthly Operating Checklist](#9-daily--weekly--monthly-operating-checklist)
10. [User Roles & Who Does What](#10-user-roles--who-does-what)
11. [Frequently Asked Questions](#11-frequently-asked-questions)
12. [Support & Contact](#12-support--contact)

---

## 1. Getting Started — First Login

### 1.1 Access the Application

1. Open your browser and go to your Salon ERP URL:  
   `https://salon.yourdomain.com`
2. Login with your ERPNext credentials (provided by your branch manager or administrator).
3. On the left sidebar, click **Salon Management** workspace.
4. You will see the **Salon Dashboard** with key shortcuts:
   - 📅 Today's Appointments
   - 🛒 POS Billing
   - 👥 Stylist Productivity
   - 📦 Inventory Alerts

---

### 1.2 Initial Salon Setup (One-Time — Admin Only)

> **Who does this:** System Administrator or Salon Owner (first time only)

| Step | Action | Where |
|---|---|---|
| 1 | Create your Company & Branches | ERPNext → Accounting → Company |
| 2 | Setup Customer Portal Settings | Customer Portal → Customer Portal Settings |
| 3 | Define Service Categories & Items | Salon Services → Service Category |
| 4 | Add Stylists & Employees | ERPNext → HR → Employee |
| 5 | Configure Appointment Slots & Policies | Appointment Booking → Booking Slot |
| 6 | Load Demo Data (Optional) | `bench execute salon_management.setup.demo_data.setup` |

---

### 1.3 Assign User Roles

> **Who does this:** Branch Manager / Administrator

Go to **ERPNext → HR → User** and assign each person their role:

| Role | Assign To |
|---|---|
| Salon Owner | CEO / Multi-Branch Owner |
| Branch Manager | Salon Branch Manager |
| Receptionist | Front Desk Staff |
| Stylist / Therapist | Service Providers / Junior Stylists |
| Inventory Manager | Store / Inventory Head |
| Accountant | Billing & Finance Team |

---

## 2. Module 1 — Appointment & Booking Management

> **Purpose:** Seamlessly manage customer bookings, slots, cues, waitlists, and reminders to ensure a zero-friction front desk operation.

---

### 2.1 SOP — Register a Walk-In Appointment

**Who:** Receptionist  
**When:** When a customer visits the salon without a prior booking

| Step | Action |
|---|---|
| 1 | Go to **Appointment Booking → Salon Appointment → + New** |
| 2 | Select **Customer** (create quickly if new) |
| 3 | Enter **Appointment Type** = Walk-In |
| 4 | Select **Service Category** and desired **Services** |
| 5 | Assign an available **Stylist** via auto-assign or manually |
| 6 | Set **Status** to "Confirmed" or "In Progress" |
| 7 | Click **Save** |

✅ **Expected Result:** Stylist receives notification. Customer is marked in the active service queue. Schedule blocks the selected slot.

---

### 2.2 SOP — Online Booking Management

**Who:** Receptionist / Automated  
**When:** As customers request appointments via Customer Portal

| Step | Action |
|---|---|
| 1 | View **Salon Appointment** dashboard |
| 2 | Filter by **Status** = "Requested" |
| 3 | Verify **Booking Slot** availability and assigned Therapist |
| 4 | Change Status to "Confirmed" |
| 5 | Save |

✅ **Expected Result:** Confirmation SMS/WhatsApp sent automatically. Slot reserved effectively in ERPNext.

---

### 2.3 SOP — Manage Rescheduling & Cancellations

**Who:** Receptionist / Customer (via portal)  
**When:** Customer calls to change time or cancel

| Step | Action |
|---|---|
| 1 | Open existing **Salon Appointment** |
| 2 | Adjust **Appointment Time** and **Stylist** |
| 3 | If Canceling, change Status to "Cancelled" and add Cancellation Reason |
| 4 | Click Save |

✅ **Expected Result:** Calendar slot freed up. Stylist schedule updated. No-show tracking activated if cancelled past the allowed cutoff.

---

### 2.4 SOP — Set Up Reminders (WhatsApp/SMS)

**Who:** Branch Manager / Admin  
**When:** One-time configuration

| Step | Action |
|---|---|
| 1 | Go to **Customer Portal Settings → Notifications** |
| 2 | Enable WhatsApp / SMS Notify |
| 3 | Add API Provider & API Keys |
| 4 | Configure **Appointment Reminder Policy** for timings (e.g., 2 hours before) |

```
Workflow: Appointment Booking ──► Confirmation SMS ──► Reminder SMS (2 Hrs Before) ──► Feedback Link (Post-service)
```

---

## 3. Module 2 — Salon Services & Treatment Management

> **Purpose:** Standardize service execution, capture customer consultation details, allocate specific stylists, and record treatment progress via checklists.

---

### 3.1 SOP — Stylist Assignment & Duty Roster

**Who:** Branch Manager / Receptionist  
**When:** Daily or for specific requests

| Step | Action |
|---|---|
| 1 | Go to **Salon Services → Stylist Assignment → + New** |
| 2 | Link to the **Salon Appointment** |
| 3 | Assign Primary **Stylist** or secondary assistants |
| 4 | Assign working station/room if applicable |
| 5 | Change Status to "Assigned" |

---

### 3.2 SOP — Record a Service Session

**Who:** Stylist / Therapist  
**When:** During or immediately after service execution

| Step | Action |
|---|---|
| 1 | Open **Service Session** from the Appointment or Dashboard |
| 2 | Update **Session Status** to "In Progress" |
| 3 | Enter **Start Time** precisely |
| 4 | Add any critical customer feedback / skin reaction / notes under consultation |
| 5 | Enter **End Time** and Change Status to "Completed" on finish |

---

### 3.3 SOP — Complete Treatment Checklist

**Who:** Stylist / Therapist  
**When:** Handling specialized treatments (e.g., Keratin, Laser Therapy)

| Step | Action |
|---|---|
| 1 | Go to **Treatment Checklist** linked to the Session |
| 2 | Confirm pre-requisites (e.g., Allergy test, hygiene prep) |
| 3 | Upload Before/After Photos securely using Image Attachments |
| 4 | Check off mandatory steps as guided by the specific Service Category |
| 5 | Validate and Save |

✅ **Expected Result:** Proper quality assurance recorded. Customer safety ensured. Standardized treatment history stored for next visit.

---

### 3.4 SOP — Multi-Service / Bridal Package Workflow

**Who:** Branch Manager  
**When:** Managing high-value bridal packages spanning multiple days

| Step | Action |
|---|---|
| 1 | Create a Master **Salon Appointment** for "Bridal Package" |
| 2 | Split into multiple **Service Sessions** for distinct dates (Pre-bridal, Mehndi, Wedding Day) |
| 3 | Assign individual **Stylist Assignments** for each session |
| 4 | Manage advance POS billing separately with wallet deposits |

---

## 4. Module 3 — Customer Membership & Loyalty Management

> **Purpose:** Build recurring revenue, incentivize repeat visits, manage prepaid wallets, and track loyalty point accrual and redemption automatically.

---

### 4.1 SOP — Onboard Customer to a Membership Plan

**Who:** Receptionist  
**When:** Customer purchases a recurring or prepaid package

| Step | Action |
|---|---|
| 1 | Go to **Customer Membership → + New** |
| 2 | Select **Customer** |
| 3 | Select **Membership Plan** (e.g., Gold Annual Membership) |
| 4 | Review the pre-populated **Included Services** and balances |
| 5 | Complete payment POS / Invoice |
| 6 | System activates membership and loads prepaid wallet credits/services |

---

### 4.2 SOP — Loyalty Point Redemption

**Who:** Receptionist  
**When:** Billing phase during checkout

| Step | Action |
|---|---|
| 1 | Check customer's total points via **Loyalty Transaction** ledger |
| 2 | At POS, enter amount to redeem in the Loyalty Point deduction option |
| 3 | Create **Loyalty Transaction** automatically on POS Save |

✅ **Expected Result:** POS total is discounted. Point balance depreciated.

---

### 4.3 SOP — Wallet Recharge & Top-Up

**Who:** Receptionist / Customer (via App)  
**When:** Customer pays advance bulk amount

| Step | Action |
|---|---|
| 1 | Go to **Salon Wallet** / Recharge Interface |
| 2 | Log Top-up amount |
| 3 | Sync with ERPNext Payment Entry |
| 4 | **Wallet Balance** gets credited |

---

### 4.4 SOP — Track Birthday & Referral Rewards

**Who:** Automated Scheduler / Receptionist  
**When:** Automatically on birthdays / manually on referrals

| Step | Action |
|---|---|
| 1 | The ERPNext cron job `loyalty_engine.py` checks for customer birthdays daily |
| 2 | Issues Birthday Bonus points defined in `Membership Plan` |
| 3 | For referrals, Receptionist attaches `Referred By` on new Customer profile |
| 4 | Referral Bonus is credited once new customer finishes first billing |

---

## 5. Module 4 — Inventory & Product Usage Management

> **Purpose:** Accurately track back-bar consumption, log chemical usage on clients, trigger low-stock alerts, and ensure exact inventory valuation for profitability.

---

### 5.1 SOP — Log Chemical Consumption on a Client

**Who:** Stylist / Therapist  
**When:** Preparing colors, keratin, or specialized chemical treatments

| Step | Action |
|---|---|
| 1 | Go to **Chemical Consumption Log → + New** |
| 2 | Select **Customer** and **Service Session** |
| 3 | Enter precise **Formula** (e.g., "Color 5/1 30g + 6% Dev 30g") |
| 4 | List specific **Items** and exact **Quantity Consumed** |
| 5 | Submit |

✅ **Expected Result:** Stock immediately deducted. Consumption cost mapped to service profitability. Exact formula saved for customer's next visit.

---

### 5.2 SOP — Record General Product Usage (Back-bar)

**Who:** Branch Manager / Stylist  
**When:** Taking out shampoo, retail product for in-house use

| Step | Action |
|---|---|
| 1 | Go to **Product Usage Entry → + New** |
| 2 | Select **Usage Date** and **Branch** |
| 3 | Enter items consumed into the product table |
| 4 | Submit |

✅ **Expected Result:** Stock Entries (Material Issue) auto-generated in ERPNext. Inventory ledger updated.

---

### 5.3 SOP — Manage Low Stock & Purchase

**Who:** Inventory Manager  
**When:** Weekly stock check

| Step | Action |
|---|---|
| 1 | Check **Stock Level** reports |
| 2 | Items dropping below auto-reorder levels flagged |
| 3 | Go to **Supplier Product Mapping** for preferred supplier |
| 4 | Generate **Material Request** → **Purchase Order** |

---

## 6. Module 5 — Customer Portal & Mobile Experience

> **Purpose:** Let customers self-book, check balances, and download invoices easily via the portal.

---

### 6.1 SOP — Enable the Customer Portal

**Who:** Admin  
**When:** One-time configuration

| Step | Action |
|---|---|
| 1 | Go to **Customer Portal Settings** |
| 2 | Tick **Portal Enabled** |
| 3 | Define Allowed Service Categories via **CP Allowed Category** child table |
| 4 | Set Authentication method (Mobile OTP / Email / Both) |
| 5 | Add Contact Phone, Display Hours, Welcome Message, Logo |

---

### 6.2 SOP — Customer Self-Booking Flow

**Who:** Customer  
**When:** Browsing online

1. Customer navigates to `https://salon.yourdomain.com/portal/book`
2. Logs in via OTP
3. Views available times via **Booking Slot** mechanism
4. Submits appointment request
5. System logs it as **Requested** in backend Appointment queue.

---

### 6.3 SOP — Manage Customer Feedback & Ratings

**Who:** Branch Manager  
**When:** Post service

| Step | Action |
|---|---|
| 1 | Auto-SMS invites customer to rate after Invoice payment |
| 2 | Customer logs 1-5 stars & comments in **Customer Feedback** via portal |
| 3 | Manager reviews feedback under **Customer Feedback** DocType |
| 4 | Bad ratings trigger automatic **Portal Notification** to Owner |

---

## 7. Module 6 — Billing & Financial Operations

> **Purpose:** Handle cash/card payments, memberships prepayments, generate tax-compliant invoices, and manage cashier limits.

---

### 7.1 SOP — POS Billing for Services

**Who:** Receptionist  
**When:** Customer checkout

| Step | Action |
|---|---|
| 1 | Open **ERPNext POS** window |
| 2 | Select the completed **Salon Appointment** (auto-pulls items) |
| 3 | Apply any active Membership / Package balances (discount logic triggers) |
| 4 | Record payment via Cash, Card, UPI, or Wallet |
| 5 | Hit **Submit** and print/email receipt |

✅ **Expected Result:** GL entries posted. Revenue recorded. Stylist commission metrics updated.

---

### 7.2 SOP — Process Refund / Cancellation

**Who:** Branch Manager  
**When:** Disputed service or package cancellation

| Step | Action |
|---|---|
| 1 | Open the paid **Sales Invoice** |
| 2 | Click **Create → Return / Credit Note** |
| 3 | Approve the return quantity/amount |
| 4 | Re-credit **Salon Wallet** OR process manual cash/bank refund via Payment Entry |
| 5 | Submit Credit Note |

---

## 8. Module 7 — Reports & Analytics

> **Purpose:** Uncover branch profitability, top-performing stylists, fast-moving services, and client retention bottlenecks.

### 8.1 Stylist Productivity Report
- **Navigation:** Reports → Stylist Productivity
- **Usage:** Run weekly to see total services handled, service time vs ideal time, revenue generated, and 5-star feedback count per stylist.

### 8.2 Client Retention Analyzer
- **Navigation:** Reports → Client Retention
- **Usage:** Identifies customers who haven't visited in 90+ Days. Integrates with SMS Notification system for win-back campaigns.

### 8.3 Membership Balance vs Liability
- **Navigation:** Reports → Membership Liabilities
- **Usage:** Essential for Accounting. Shows unredeemed wallet balances and unutilized package services to calculate deferred revenue.

### 8.4 Product Usage vs Revenue
- **Navigation:** Reports → Product Usage vs Revenue
- **Usage:** Compare high material-cost treatments (e.g. hair coloring, keratin) against billed revenue.

---

## 9. Daily / Weekly / Monthly Operating Checklist

### 9.1 Daily (5–10 minutes)

| Task | Who | Where |
|---|---|---|
| ☐ Review upcoming appointments for the day | Receptionist | Appointment Booking list |
| ☐ Assign unassigned Walk-ins to Stylists | Receptionist | Stylist Assignment |
| ☐ Ensure all completed services are Billed | Receptionist | POS / Invoices |
| ☐ Review bad customer feedback given today | Branch Manager | Customer Feedback |
| ☐ Handle "No-Shows" marking them accurately | Receptionist | Salon Appointment |

---

### 9.2 Weekly (30 minutes)

| Task | Who | Where |
|---|---|---|
| ☐ Review Low Stock levels and trigger Purchase Orders | Inventory Mgr | Stock Report |
| ☐ Verify Product Usage Entries and Chemical Logs are submitted | Inventory Mgr | Product Usage Entry |
| ☐ Calculate Stylist Incentives & Productivity | Branch Manager | Stylist Report |
| ☐ Resolve portal issues or appointment disputes | Branch Manager | Customer Support |

---

### 9.3 Monthly (1–2 hours)

| Task | Who | Where |
|---|---|---|
| ☐ Reconcile Cash Payments vs ERPNext GL | Accountant | Banking |
| ☐ Run the Revenue vs Target report | Owner | Analytics |
| ☐ Review expiring memberships and run renewal SMS campaign | Receptionist | Customer Membership |
| ☐ P&L generation and branch-wise profit analysis | Accountant | ERPNext Accounting |

---

### 9.4 Quarterly / Annually (Full day)

| Task | Who | Where |
|---|---|---|
| ☐ Full Physical Inventory Audit | Inventory Mgr | Stock Reconciliation |
| ☐ Assess service pricing against inflation/costs | Owner | Service Category |
| ☐ Stylist / Therapist Performance Appraisals | HR / Owner | Employee Review |

---

## 10. User Roles & Who Does What

| Feature | Owner / Admin | Branch Manager | Receptionist | Stylist | Inventory Manager | Accountant |
|---|---|---|---|---|---|---|
| Customer Portal Options | ✅ Full | 👁 Read | ❌ | ❌ | ❌ | ❌ |
| Membership & Plans | ✅ Full | ✅ Full | 👁 Read | ❌ | ❌ | 👁 Read |
| Appointment Book | ✅ Full | ✅ Full | ✅ Full | 👁 Read | ❌ | ❌ |
| Stylist Assignment | ✅ Full | ✅ Full | ✅ Full | 👁 View Own | ❌ | ❌ |
| Chemical/Treatment Log | ✅ Full | 👁 Read | ❌ | ✅ Full | 👁 Read | ❌ |
| Product Usage Entry | ✅ Full | ✅ Full | ❌ | ✅ Create | ✅ Full | 👁 Read |
| POS & Sales Invoices | ✅ Full | ✅ Full | ✅ Full | ❌ | ❌ | ✅ Full |
| Financial Reports | ✅ Full | 👁 Read | ❌ | ❌ | ❌ | ✅ Full |

---

## 11. Frequently Asked Questions

**Q1: A customer's requested appointment slot is unavailable on the portal. Why?**  
A: Ensure the `Booking Slot` is active, the `Service Category` isn't blocked, and the assigned stylist/therapist status isn't mapping to a leave application in ERPNext HR.

---

**Q2: How do I reassign a stylist if one calls in sick?**  
A: Go to `Stylist Assignment`, open the active record for the booking, cancel it or reassign it by selecting a new employee, and hit save. The schedule updates immediately.

---

**Q3: Loyalty points are not updating after a transaction.**  
A: Check if the `Customer Membership` plan is active, and confirm if `loyalty_engine.py` background scheduled jobs are running. Also ensure POS transactions are marked "Submit" and not just drafted.

---

**Q4: Customer wallet balance is showing a mismatch.**  
A: Run the `Salon Wallet` transaction ledger report. Every deduction must have an associated Sales Invoice, and every top-up strictly requires a Payment Entry. If manually adjusted, verify Journal Entries.

---

**Q5: A refund was initiated but wallet not credited.**  
A: Go to the Sales Invoice, click Create Return (Credit Note). When receiving the Payment Entry for the return, ensure you allocate it back directly to the Customer's Wallet advance account.

---

**Q6: A prepaid membership package balance (e.g. 5 haircuts left) is not reflecting during POS.**  
A: The customer must be linked correctly. Ensure `Plan Service Inclusion` specifies the exact mapped `Service Item` being billed at the POS.

---

**Q7: Service is complete but invoice isn't generated.**  
A: Receptionist needs to fetch the `Salon Appointment` into the POS. Completing a `Service Session` updates the workflow state but does not create financial accounting records automatically.

---

**Q8: Chemical inventory deduction seems incorrect.**  
A: Verify the `Chemical Consumption Log`. Stylists must enter exact grams/ml. If using default UOM (e.g. Bottles), it will over-consume stock. Ensure stock UOMs match consumption UOMs.

---

**Q9: How exactly does No-Show handling work?**  
A: If a customer doesn't arrive past the `Cancellation Cutoff Hours` set in `Customer Portal Settings` (e.g. 2 hours), the receptionist marks Appointment Status = "No Show". This triggers standard penalty protocols depending on your config.

---

**Q10: When and how are appointment reminders triggered?**  
A: Standard logic checks the `Appointment Reminder Policy`. If configured for "24 Hours Before", an automated scheduler sends WhatsApp/Email utilizing templates at exactly `Start_Time - 24H`.

---

**Q11: How do we renew expired memberships?**  
A: Create a NEW `Customer Membership` pulling from the same `Membership Plan` template. The system handles historic data, adding active days onto the customer record.

---

**Q12: How to handle multi-day Bridal Package scheduling?**  
A: The Master Appointment acts as a directory. Use multiple `Service Sessions` mapped to different days. Do not cram 3 days of events into one session record.

---

**Q13: How to update Service Pricing without breaking old invoices?**  
A: Update the Price List in ERPNext Standard configuration or update the default `Service Category` pricing. Historic POS/Invoices capture pricing at submission time and freeze it.

---

**Q14: How to address or reopen customer complaints from bad ratings?**  
A: Navigate to `Customer Feedback`, review the text. Add internal communication/comments. Change status to "In Review" or "Resolved". If necessary, grant manual `Loyalty Transaction` points as an apology.

---

**Q15: How to export salon analytics for external investor reports?**  
A: Go to any Report (e.g., Stylist Productivity), click the "Menu" (three dots) -> "Export", and select CSV or Excel format.

---

## 12. Support & Contact

| Channel | Details |
|---|---|
| 📧 Email | support@salonbiz.in |
| 📖 Documentation | https://docs.salonbiz.in/user-guide |
| 🐛 Bug Reports | https://github.com/nick200555/Salon/issues |
| 📱 WhatsApp | +91-XXXXXXXXXX (Central ERP Support) |

---

*© 2026 Salon ERP — Built for modern beauty and wellness operations*  
*Powered by Frappe Framework & ERPNext v15*
