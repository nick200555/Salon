import frappe
from frappe.utils import nowdate, add_days

def flag_no_shows():
	"""Mark appointments as No-Show if customer didn't arrive."""
	appointments = frappe.get_all("Salon Appointment", 
		filters={"status": ["in", ["Booked", "Confirmed"]], "appointment_date": ["<", nowdate()]},
		fields=["name"]
	)
	for appt in appointments:
		frappe.db.set_value("Salon Appointment", appt.name, "status", "No-Show")
	
	if appointments:
		frappe.db.commit()

def update_appointment_aging():
	"""Update queue status for long-waiting appointments."""
	pass
