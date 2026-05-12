import json
import os

content = [
    {"id": "cb-appointment", "type": "card", "data": {"card_name": "Appointment & Booking", "col": 12}},
    {"id": "cb-services", "type": "card", "data": {"card_name": "Salon Services", "col": 12}},
    {"id": "cb-membership", "type": "card", "data": {"card_name": "Membership & Loyalty", "col": 12}},
    {"id": "cb-inventory", "type": "card", "data": {"card_name": "Inventory & Products", "col": 12}},
    {"id": "cb-experience", "type": "card", "data": {"card_name": "Customer Experience", "col": 12}},
    {"id": "cb-billing", "type": "card", "data": {"card_name": "Billing & Finance", "col": 12}},
    {"id": "cb-reports", "type": "card", "data": {"card_name": "Reports & Analytics", "col": 12}},
    {"id": "cb-staff", "type": "card", "data": {"card_name": "Staff & Operations", "col": 12}},
    {"id": "cb-config", "type": "card", "data": {"card_name": "Configuration", "col": 12}}
]

sections = [
    ("Appointment & Booking", ["Salon Appointment", "Booking Slot", "Walk-In Queue", "Appointment Reminder Policy", "Appointment Cancellation"]),
    ("Salon Services", ["Service Session", "Service Item", "Stylist Assignment", "Treatment Checklist", "Bridal Package"]),
    ("Membership & Loyalty", ["Membership Plan", "Customer Membership", "Loyalty Transaction", "Salon Wallet", "Referral Reward"]),
    ("Inventory & Products", ["Product Usage Entry", "Salon Inventory Batch", "Chemical Consumption Log", "Supplier Product Mapping", "Product Expiry Tracker"]),
    ("Customer Experience", ["Customer Feedback", "Portal Notification", "Customer Portal Settings", "Stylist Rating", "Service Review"]),
    ("Billing & Finance", ["POS Invoice", "Service Invoice", "Package Billing", "Refund Request", "Daily Cash Reconciliation"]),
    ("Reports & Analytics", ["Daily Appointment Report", "Stylist Productivity", "Revenue by Service", "Membership Renewal Tracker", "Peak Hours Analytics"]),
    ("Staff & Operations", ["Employee Schedule", "Staff Attendance", "Branch Performance", "Salon Shift Management", "Task Assignment"]),
    ("Configuration", ["Salon Management Settings"])
]

links = []
idx = 1
for sec_name, sec_links in sections:
    # Card Break
    links.append({
        "hidden": 0,
        "idx": idx,
        "is_query_report": 0,
        "label": sec_name,
        "link_count": 0,
        "onboard": 1 if idx <= 20 else 0,
        "title": sec_name,
        "type": "Card Break"
    })
    idx += 1
    # Links
    for link_name in sec_links:
        link_type = "DocType"
        if "Report" in link_name or "Analytics" in link_name or "Tracker" in link_name or "Log" in link_name:
            # Let's assume some are reports, but standard is DocType. The prompt says to use DocType generally unless report.
            # I will just use DocType for simplicity, or check if it explicitly says Report.
            if "Report" in link_name or "Analytics" in link_name:
                link_type = "Report"
                is_query_report = 1
            else:
                link_type = "DocType"
                is_query_report = 0
        else:
            link_type = "DocType"
            is_query_report = 0

        links.append({
            "dependencies": "",
            "hidden": 0,
            "idx": idx,
            "is_query_report": is_query_report,
            "label": link_name,
            "link_count": 0,
            "link_to": link_name,
            "link_type": link_type,
            "onboard": 1 if idx <= 20 else 0,
            "type": "Link"
        })
        idx += 1

shortcuts = [
    {
        "color": "Blue",
        "format": "{} Today's",
        "label": "Salon Appointment",
        "link_to": "Salon Appointment",
        "stats_filter": "{\"appointment_date\": [\"=\", \"Today\"]}",
        "type": "DocType"
    },
    {
        "color": "Green",
        "format": "{} Active",
        "label": "Customer Membership",
        "link_to": "Customer Membership",
        "stats_filter": "{\"status\": \"Active\"}",
        "type": "DocType"
    },
    {
        "color": "Orange",
        "format": "{} Pending",
        "label": "POS Invoice",
        "link_to": "POS Invoice",
        "stats_filter": "{\"status\": \"Unpaid\"}",
        "type": "DocType"
    },
    {
        "color": "Red",
        "format": "{} Open",
        "label": "Refund Request",
        "link_to": "Refund Request",
        "stats_filter": "{\"status\": \"Open\"}",
        "type": "DocType"
    },
    {
        "color": "Purple",
        "format": "{} Low Stock",
        "label": "Product Usage Entry",
        "link_to": "Product Usage Entry",
        "stats_filter": "{\"stock_status\": \"Low\"}",
        "type": "DocType"
    },
    {
        "color": "Blue",
        "label": "Stylist Assignment",
        "link_to": "Stylist Assignment",
        "type": "DocType"
    },
    {
        "color": "Gray",
        "label": "Customer Feedback",
        "link_to": "Customer Feedback",
        "type": "DocType"
    },
    {
        "color": "Green",
        "label": "Service Invoice",
        "link_to": "Service Invoice",
        "type": "DocType"
    }
]

workspace_json = {
 "charts": [],
 "content": json.dumps(content),
 "creation": "2024-01-01 00:00:00.000000",
 "developer_mode_only": 0,
 "disable_user_customization": 0,
 "docstatus": 0,
 "doctype": "Workspace",
 "for_user": "",
 "hide_custom": 0,
 "icon": "beauty",
 "idx": 0,
 "is_default": 0,
 "is_hidden": 0,
 "label": "Salon Management",
 "links": links,
 "modified": "2024-01-01 00:00:00.000000",
 "modified_by": "Administrator",
 "module": "Salon Management",
 "name": "Salon Management",
 "owner": "Administrator",
 "public": 1,
 "restrict_to_domain": "",
 "roles": [],
 "sequence_id": 1.0,
 "shortcuts": shortcuts,
 "title": "Salon Management"
}

dir_path = r"c:\Seria Internship\Salon\salon_management\salon_management\salon_management\workspace\salon_management"
os.makedirs(dir_path, exist_ok=True)

with open(os.path.join(dir_path, "salon_management.json"), "w", encoding="utf-8") as f:
    json.dump(workspace_json, f, indent=1)

print("JSON created successfully")
