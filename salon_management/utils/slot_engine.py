import frappe
from frappe.utils import now_datetime, get_time, add_to_date

def reserve_booking_slot(doc, method=None):
    """Reserve a Booking Slot on Salon Appointment creation."""
    if not doc.appointment_date or not doc.appointment_time:
        return

    # Check for existing slot in booking slot master
    slots = frappe.get_list('Booking Slot',
        filters={
            'branch': doc.branch,
            'day_of_week': doc.appointment_date.strftime('%A'),
            'slot_start': doc.appointment_time,
            'is_active': 1,
            'is_blocked': 0
        },
        fields=['name', 'max_concurrent'])
    
    if not slots:
        frappe.throw('No available slot found for the selected time and branch.')
    
    # Check current occupancy
    booked = frappe.db.count('Salon Appointment', {
        'appointment_date': doc.appointment_date,
        'appointment_time': doc.appointment_time,
        'branch': doc.branch,
        'status': ['not in', ['Cancelled', 'No-Show']]
    })
    
    if booked >= slots[0]['max_concurrent']:
        frappe.throw(f"All slots for {doc.appointment_time} are fully booked.")
        
    doc.slot_ref = slots[0]['name']

def get_open_slots(branch, service_category, appointment_date):
    """Return list of open slots for portal booking."""
    if isinstance(appointment_date, str):
        appointment_date = frappe.utils.getdate(appointment_date)
        
    cat = frappe.get_doc('Service Category', service_category)
    all_slots = frappe.get_list('Booking Slot',
        filters={
            'branch': branch,
            'day_of_week': appointment_date.strftime('%A'),
            'is_active': 1, 
            'is_blocked': 0
        },
        fields=['name', 'slot_start', 'slot_end', 'max_concurrent'],
        order_by='slot_start asc')
    
    open_slots = []
    for slot in all_slots:
        booked = frappe.db.count('Salon Appointment', {
            'appointment_date': appointment_date,
            'appointment_time': slot['slot_start'],
            'branch': branch,
            'status': ['not in', ['Cancelled', 'No-Show']]
        })
        if booked < slot['max_concurrent']:
            open_slots.append(slot)
    return open_slots

def release_expired_slot_holds():
    """Scheduled: release unconfirmed bookings older than 15 minutes."""
    cutoff = add_to_date(now_datetime(), minutes=-15)
    stale = frappe.get_list('Salon Appointment',
        filters={'status': 'Booked', 'creation': ['<', cutoff]},
        fields=['name'])
    
    for appt in stale:
        frappe.db.set_value('Salon Appointment', appt.name, 'status', 'Cancelled')
        frappe.db.set_value('Salon Appointment', appt.name,
            'cancellation_reason', 'Auto-cancelled: booking not confirmed within 15 minutes')
    
    frappe.db.commit()
