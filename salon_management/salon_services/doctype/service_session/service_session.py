import frappe
from frappe.model.document import Document

class ServiceSession(Document):
    def validate(self):
        self.total_services = len(self.services_performed)
        self.update_checklist_status()

    def update_checklist_status(self):
        """Checks if all mandatory checklist items are ticked."""
        # Logic to check treatment checklist items
        pass

    def on_submit(self):
        self.create_product_usage_entry()
        self.update_appointment_status()

    def create_product_usage_entry(self):
        """Auto-creates Product Usage Entry on Session submit."""
        if not self.products_used:
            return
            
        usage = frappe.new_doc('Product Usage Entry')
        usage.service_session = self.name
        usage.branch = self.branch
        usage.usage_date = self.session_date
        usage.stylist = self.primary_stylist
        
        for p in self.products_used:
            usage.append('products', {
                'item': p.item,
                'batch_no': p.batch_no,
                'qty_used': p.qty_used,
                'uom': p.uom
            })
            
        usage.insert(ignore_permissions=True)
        usage.submit()

    def update_appointment_status(self):
        """Updates the status of the linked Salon Appointment."""
        if self.appointment:
            frappe.db.set_value('Salon Appointment', self.appointment, 'status', 'Completed')
            frappe.db.set_value('Salon Appointment', self.appointment, 'service_end_time', self.session_end)
