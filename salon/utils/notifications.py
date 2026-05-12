import frappe
from frappe import _

def send_booking_confirmation(doc, method=None):
    """Sends WhatsApp/email confirmation to customer immediately."""
    customer_mobile = doc.customer_mobile or frappe.db.get_value('Customer', doc.customer, 'mobile_no')
    if not customer_mobile:
        return
        
    message = _("Hi {0}, your appointment {1} at {2} on {3} at {4} is booked.").format(
        doc.customer, doc.name, doc.branch, 
        frappe.utils.format_date(doc.appointment_date),
        frappe.utils.format_time(doc.appointment_time)
    )
    
    log_notification(doc.customer, "Appointment Confirmed", "WhatsApp", doc.name, message)
    # Actual API call to WhatsApp provider would go here

def notify_stylist_on_confirmation(doc, method=None):
    """Sends WhatsApp notification to assigned stylist on confirmation."""
    if doc.status != "Confirmed":
        return
        
    stylist_mobile = frappe.db.get_value('Employee', doc.primary_stylist, 'cell_number')
    if not stylist_mobile:
        return
        
    message = _("New appointment assigned: {0} for {1} at {2}.").format(
        doc.name, doc.customer, doc.appointment_time
    )
    
    # Logic to send WhatsApp
    # log_notification(...)

def send_appointment_reminders():
    """Dispatches reminder 1 and reminder 2 based on policy timing."""
    # Find appointments that need reminders based on their policy
    pass

def log_notification(customer, ntype, channel, source_doc, message):
    notification = frappe.new_doc('Portal Notification')
    notification.customer = customer
    notification.notification_type = ntype
    notification.channel = channel
    notification.source_document = source_doc
    notification.message = message
    notification.sent_at = frappe.utils.now_datetime()
    notification.delivery_status = "Sent"
    notification.insert(ignore_permissions=True)

def notify_membership_status(doc, method=None):
    """Notify customer about membership activation/expiry."""
    pass

def send_membership_expiry_reminders():
    """Daily job to find expiring memberships and send alerts."""
    pass
