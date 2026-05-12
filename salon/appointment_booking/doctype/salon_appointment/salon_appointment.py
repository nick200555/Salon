import frappe
from frappe.model.document import Document
from frappe.utils import get_time, add_to_date, now_datetime

class SalonAppointment(Document):
    def validate(self):
        self.calculate_end_time()
        self.check_repeat_customer()
        
    def calculate_end_time(self):
        """Calculates end time based on service durations."""
        if not self.appointment_time:
            return
            
        total_duration = sum([d.duration_mins or 0 for d in self.services])
        if total_duration == 0:
            # Fetch from service category if table is empty
            total_duration = frappe.db.get_value('Service Category', self.service_category, 'default_duration_mins') or 60
            
        self.end_time = add_to_date(None, seconds=get_time(self.appointment_time).second + (total_duration * 60))
        # End time calculation usually needs a reference date. 
        # For simplicity in this logic, we just handle the time portion.
        
    def check_repeat_customer(self):
        count = frappe.db.count('Salon Appointment', {
            'customer': self.customer,
            'status': 'Completed',
            'name': ['!=', self.name]
        })
        self.is_repeat_customer = 1 if count > 0 else 0

    def on_submit(self):
        if self.status == "Completed":
            self.create_pos_invoice_on_completion()

    def create_pos_invoice_on_completion(self):
        """Creates ERPNext POS Invoice for completed appointment."""
        if self.pos_invoice:
            return
            
        # Logic to create POS Invoice
        # This would typically involve gathering items from the services table
        pass

    @frappe.whitelist()
    def update_queue_position(self):
        """Recalculates walk-in queue positions on status change."""
        if self.booking_channel == "Walk-In" and self.status == "Booked":
            today_completed = frappe.db.count('Salon Appointment', {
                'appointment_date': self.appointment_date,
                'branch': self.branch,
                'booking_channel': 'Walk-In',
                'status': 'Completed'
            })
            self.queue_position = today_completed + 1
