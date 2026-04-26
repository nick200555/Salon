import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return [
        {"label": _("Appointment No"), "fieldname": "name", "fieldtype": "Link", "options": "Salon Appointment", "width": 150},
        {"label": _("Customer"), "fieldname": "customer", "fieldtype": "Link", "options": "Customer", "width": 150},
        {"label": _("Branch"), "fieldname": "branch", "fieldtype": "Link", "options": "Branch", "width": 120},
        {"label": _("Date"), "fieldname": "appointment_date", "fieldtype": "Date", "width": 100},
        {"label": _("Time"), "fieldname": "appointment_time", "fieldtype": "Time", "width": 100},
        {"label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 100},
        {"label": _("Stylist"), "fieldname": "primary_stylist", "fieldtype": "Link", "options": "Employee", "width": 150},
        {"label": _("Check-in"), "fieldname": "check_in_time", "fieldtype": "Datetime", "width": 150}
    ]

def get_data(filters):
    conditions = {}
    if filters.get('from_date') and filters.get('to_date'):
        conditions['appointment_date'] = ['between', [filters.get('from_date'), filters.get('to_date')]]
    elif filters.get('date'):
        conditions['appointment_date'] = filters.get('date')
        
    if filters.get('branch'):
        conditions['branch'] = filters.get('branch')
    if filters.get('status'):
        conditions['status'] = filters.get('status')
        
    return frappe.get_all('Salon Appointment',
        filters=conditions,
        fields=['name', 'customer', 'branch', 'appointment_date', 'appointment_time', 'status', 'primary_stylist', 'check_in_time'],
        order_by='appointment_time asc')
