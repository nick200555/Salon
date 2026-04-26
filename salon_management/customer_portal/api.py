import frappe
from frappe import _

@frappe.whitelist(allow_guest=False)
def get_customer_appointments(customer_mobile=None):
    """Return all appointments for the authenticated customer."""
    user = frappe.session.user
    customer = frappe.db.get_value('Customer', {'user_id': user}, 'name')
    if not customer:
        return []
        
    return frappe.get_list('Salon Appointment',
        filters={'customer': customer},
        fields=['name', 'appointment_date', 'appointment_time', 'status', 'primary_stylist', 'branch', 'service_category'],
        order_by='appointment_date desc')

@frappe.whitelist(allow_guest=False)
def create_appointment(branch, service_category, appointment_date, appointment_time, notes=None):
    """Create a new appointment from the customer portal."""
    user = frappe.session.user
    customer = frappe.db.get_value('Customer', {'user_id': user}, 'name')
    if not customer:
        frappe.throw(_("Please contact support to register your customer account."))
        
    doc = frappe.new_doc('Salon Appointment')
    doc.customer = customer
    doc.branch = branch
    doc.service_category = service_category
    doc.appointment_date = appointment_date
    doc.appointment_time = appointment_time
    doc.booking_channel = 'Portal'
    doc.customer_notes = notes
    doc.insert(ignore_permissions=True)
    return doc.name

@frappe.whitelist(allow_guest=False)
def get_membership_status():
    """Return active membership details."""
    user = frappe.session.user
    customer = frappe.db.get_value('Customer', {'user_id': user}, 'name')
    if not customer:
        return None
        
    return frappe.db.get_value('Customer Membership',
        {'customer': customer, 'status': 'Active'},
        ['name', 'plan', 'expiry_date', 'sessions_remaining', 'loyalty_points_balance', 'wallet_balance'],
        as_dict=True)

@frappe.whitelist(allow_guest=False)
def get_available_slots(branch, service_category, appointment_date):
    """Return available time slots."""
    from salon_management.utils.slot_engine import get_open_slots
    return get_open_slots(branch, service_category, appointment_date)
