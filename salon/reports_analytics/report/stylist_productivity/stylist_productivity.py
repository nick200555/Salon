import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    chart = get_chart(data)
    return columns, data, None, chart

def get_columns():
    return [
        {"label": _("Stylist"), "fieldname": "stylist", "fieldtype": "Link", "options": "Employee", "width": 200},
        {"label": _("Sessions Count"), "fieldname": "sessions_count", "fieldtype": "Int", "width": 120},
        {"label": _("Total Revenue"), "fieldname": "total_revenue", "fieldtype": "Currency", "width": 150},
        {"label": _("Avg Rating"), "fieldname": "avg_rating", "fieldtype": "Float", "width": 100},
        {"label": _("No-Show Rate %"), "fieldname": "no_show_rate", "fieldtype": "Percent", "width": 120}
    ]

def get_data(filters):
    # This is a sample query. In production, it would join Service Session and Feedback.
    data = []
    stylists = frappe.get_all('Employee', filters={'designation': ['in', ['Stylist', 'Therapist']]}, fields=['name', 'employee_name'])
    
    for s in stylists:
        sessions = frappe.db.count('Service Session', {'primary_stylist': s.name, 'docstatus': 1})
        revenue = frappe.db.sql("""select sum(total_cost) from `tabProduct Usage Entry` where stylist=%s and docstatus=1""", s.name)[0][0] or 0
        rating = frappe.db.sql("""select avg(overall_rating) from `tabCustomer Feedback` where stylist=%s""", s.name)[0][0] or 0
        
        data.append({
            'stylist': s.name,
            'sessions_count': sessions,
            'total_revenue': revenue,
            'avg_rating': rating,
            'no_show_rate': 0.0 # Placeholder
        })
    return data

def get_chart(data):
    return {
        "data": {
            "labels": [d['stylist'] for d in data],
            "datasets": [
                {"name": _("Revenue"), "values": [d['total_revenue'] for d in data]}
            ]
        },
        "type": "bar",
        "colors": ["#7cd6fd"]
    }
