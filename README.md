# Salon & Beauty Parlour Management System (SBPMS)

SBPMS is a comprehensive Salon and Spa Management extension for ERPNext v15, designed for high-end parlours, spas, and wellness centers. It bridges the gap between ERPNext's core accounting/stock features and the specific operational needs of the beauty industry.

## 🚀 Version Compatibility
- Frappe Framework v15+
- ERPNext v15+

---

## ✨ Features Breakdown

### 📅 Appointment & Booking
- **Smart Slot Selection**: Real-time availability check via `Booking Slot` master.
- **Auto-Stylist Assignment**: Match customers with their preferred or available stylists based on designation.
- **Queue Management**: Specialized handling for Walk-In customers with position tracking.
- **Multi-Policy Reminders**: Configurable WhatsApp/SMS/Email alerts at fixed intervals before appointments.

### 💇 Salon Services (Execution)
- **Service Sessions**: Digital execution logs with Before/After media attachments.
- **Treatment Checklists**: Enforce standard operating procedures (SOPs) for every treatment type.
- **Signature Sign-off**: Electronic customer sign-off on service completion.

### 💎 Membership & Loyalty
- **Flexible Plans**: Support for Subscriptions, Prepaid Wallets, and Service Packages.
- **Loyalty Engine**: Multiplier-based points earning system based on membership tier.
- **Wallet System**: Integrated prepaid wallet for cashless transactions.

### 📦 Inventory & Consumables
- **Chemical Tracking**: Log precise chemical consumption (grams/ml) for every hair/skin service.
- **Automated Stock Deduction**: Generates `Material Issue` Stock Entries in ERPNext upon session submission.
- **Batch Management**: Track expiry of beauty products with automated alerts.

---

## 🌐 Customer Portal (Self-Service)
The portal provides a premium, responsive experience for your clients:
- `/book`: Real-time booking wizard with slot selection.
- `/membership`: Dashboard showing loyalty points, wallet balance, and active plans.
- `/feedback`: Post-service rating and review system.

---

## 🛠 Installation & Setup

### Bench Commands
```bash
# Get the app
bench get-app https://github.com/nick200555/Salon.git salon_management

# Install on a site
bench --site [your-site] install-app salon_management

# Run migrations
bench --site [your-site] migrate

# Build assets
bench build --app salon_management

# Restart bench
bench restart
```

### Initial Configuration
After installation, run the seed script to load masters:
```bash
bench --site [your-site] execute salon_management.setup.demo_data.load_demo_data
```

---

## 📊 Modules & Reports
1. **Appointment Booking**: Naming Series `APPT-`
2. **Salon Services**: Naming Series `SESS-`
3. **Membership Loyalty**: Naming Series `MEM-`, `LTXN-`, `WLET-`
4. **Inventory Management**: Naming Series `PUSG-`, `SBAT-`
5. **Customer Portal**: Portal Settings & Feedback
6. **Reports & Analytics**: 
   - `Daily Appointment Report`
   - `Stylist Productivity`
   - `Customer Redemption Summary`

---

## 🔗 API Overview (Portal)
- `get_available_slots(branch, category, date)`: Returns list of unoccupied slots.
- `create_appointment(...)`: Portal booking endpoint.
- `get_membership_status()`: Customer balance and status check.

---

## 👨‍💻 Developer Notes
- **Utilities**: Core logic resides in `salon_management/utils/`.
- **Fixtures**: Standard Roles and Custom Fields are bundled in `fixtures/`.
- **Hooks**: Extensive use of `doc_events` for real-time stock and accounting integration.

---
© 2026 Salon Management System. Built with ❤️ on Frappe.
