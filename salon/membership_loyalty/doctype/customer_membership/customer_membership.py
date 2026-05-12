import frappe
from frappe.model.document import Document
from frappe.utils import add_days, getdate

class CustomerMembership(Document):
    def validate(self):
        self.calculate_expiry_date()
        if not self.sessions_included:
            self.sessions_included = frappe.db.get_value('Membership Plan', self.plan, 'service_limit') or 0

    def calculate_expiry_date(self):
        if self.enrollment_date and self.plan:
            validity = frappe.db.get_value('Membership Plan', self.plan, 'validity_days') or 0
            self.expiry_date = add_days(self.enrollment_date, validity)

    def on_submit(self):
        self.activate_membership_benefits()

    def activate_membership_benefits(self):
        """Credits wallet top-up and multiplier setup."""
        plan = frappe.get_doc('Membership Plan', self.plan)
        if plan.wallet_topup > 0:
            wallet_txn = frappe.new_doc('Salon Wallet')
            wallet_txn.customer = self.customer
            wallet_txn.membership = self.name
            wallet_txn.transaction_type = 'Top-Up'
            wallet_txn.amount = plan.wallet_topup
            wallet_txn.notes = f"Initial top-up for {self.plan}"
            wallet_txn.insert(ignore_permissions=True)
            
        # Update Customer record status
        frappe.db.set_value('Customer', self.customer, {
            'membership_status': plan.plan_name,
            'preferred_stylist': self.preferred_stylist
        })
