import frappe
from frappe import _

def load_demo_data():
    """Seed sample data for SBPMS."""
    create_categories()
    create_plans()
    create_slots()
    print("Demo data loaded successfully.")

def create_categories():
    categories = [
        {"name": "Hair Cut", "duration": 45, "dept": "Hair"},
        {"name": "Facial", "duration": 60, "dept": "Skin"},
        {"name": "Massage", "duration": 90, "dept": "Spa"}
    ]
    for c in categories:
        if not frappe.db.exists('Service Category', c['name']):
            doc = frappe.new_doc('Service Category')
            doc.category_name = c['name']
            doc.default_duration_mins = c['duration']
            doc.department = c['dept']
            doc.insert()

def create_plans():
    plans = [
        {"name": "Silver Monthly", "type": "Monthly Subscription", "price": 1000},
        {"name": "Gold Annual", "type": "Annual Subscription", "price": 10000}
    ]
    for p in plans:
        if not frappe.db.exists('Membership Plan', p['name']):
            doc = frappe.new_doc('Membership Plan')
            doc.plan_name = p['name']
            doc.plan_type = p['type']
            doc.price = p['price']
            doc.validity_days = 30 if "Monthly" in p['name'] else 365
            doc.insert()

def create_slots():
    # Placeholder for slot creation logic
    pass
