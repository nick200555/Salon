from . import __version__ as app_version

app_name = "salon"
app_title = "Salon & Beauty Parlour Management System"
app_publisher = "Your Company Name"
app_description = "Salon and spa post-booking customer management application"
app_email = "contact@yourcompany.com"
app_license = "mit"

# Apps
# ------------------
required_apps = ["frappe", "erpnext"]

# Roles
# ------------------
roles = [
    "Salon Manager",
    "Branch Manager",
    "Receptionist",
    "Stylist",
    "Spa Therapist",
    "Inventory Manager",
    "Accountant",
    "Customer",
]

# Fixtures
# ------------------
fixtures = [
    "Custom Field",
    "Property Setter",
    "Role",
    "Workflow",
    "Workspace",
]

# DocType Events
# ------------------
doc_events = {
    "Salon Appointment": {
        "before_insert": "salon.utils.slot_engine.reserve_booking_slot",
        "on_insert": "salon.utils.notifications.send_booking_confirmation",
        "on_update": [
            "salon.utils.notifications.notify_stylist_on_confirmation",
            "salon.appointment_booking.doctype.salon_appointment.salon_appointment.update_queue_position"
        ],
        "on_submit": [
            "salon.appointment_booking.doctype.salon_appointment.salon_appointment.create_pos_invoice_on_completion",
            "salon.utils.loyalty_engine.award_loyalty_points"
        ],
    },
    "Service Session": {
        "on_submit": [
            "salon.salon_services.doctype.service_session.service_session.create_product_usage_entry",
            "salon.salon_services.doctype.service_session.service_session.update_appointment_status"
        ],
        "on_update": "salon.salon_services.doctype.service_session.service_session.update_checklist_status",
    },
    "Customer Membership": {
        "on_submit": "salon.membership_loyalty.doctype.customer_membership.customer_membership.activate_membership_benefits",
        "before_save": "salon.membership_loyalty.doctype.customer_membership.customer_membership.calculate_expiry_date",
        "on_update": "salon.utils.notifications.notify_membership_status",
    },
    "Product Usage Entry": {
        "on_submit": "salon.inventory_management.doctype.product_usage_entry.product_usage_entry.create_stock_entry_on_submit",
        "on_cancel": "salon.inventory_management.doctype.product_usage_entry.product_usage_entry.cancel_stock_entry",
        "on_update": "salon.inventory_management.doctype.product_usage_entry.product_usage_entry.update_session_product_cost",
    },
    "Loyalty Transaction": {
        "after_insert": "salon.utils.loyalty_engine.update_customer_points_balance",
    },
    "Salon Wallet": {
        "after_insert": "salon.membership_loyalty.doctype.salon_wallet.salon_wallet.update_customer_wallet_balance",
    },
}

# Scheduler Events
# ------------------
scheduler_events = {
    "cron": {
        "*/30 * * * *": [
            "salon.utils.notifications.send_appointment_reminders",
            "salon.appointment_booking.tasks.flag_no_shows",
        ],
        "0 * * * *": [
            "salon.utils.slot_engine.release_expired_slot_holds",
        ],
    },
    "daily": [
        "salon.utils.notifications.send_membership_expiry_reminders",
        "salon.inventory_management.tasks.check_expiry_batches",
        "salon.inventory_management.tasks.check_low_stock_levels",
        "salon.membership_loyalty.tasks.process_birthday_bonuses",
        "salon.membership_loyalty.tasks.process_auto_renewals",
        "salon.appointment_booking.tasks.update_appointment_aging",
    ],
    "weekly": [
        "salon.reports_analytics.tasks.generate_weekly_kpi_report",
        "salon.inventory_management.tasks.send_consumption_summary",
    ],
}

# Website
# ------------------
website_route_rules = [
    {"from_route": "/book", "to_route": "salon_portal"},
    {"from_route": "/book/<appointment_no>", "to_route": "appointment_detail"},
    {"from_route": "/membership", "to_route": "membership_dashboard"},
]

# Notifications
# ------------------
# notification_config = "salon.salon.notification_config"

# Overrides
# ------------------
# override_doctype_class = {
#     "Customer": "salon.overrides.customer.CustomCustomer"
# }

# Static Assets
# ------------------
# app_include_js = "/assets/salon/js/salon.js"
# app_include_css = "/assets/salon/css/salon.css"

