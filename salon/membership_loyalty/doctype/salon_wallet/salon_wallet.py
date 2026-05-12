import frappe
from frappe.model.document import Document

class SalonWallet(Document):
    def on_update(self):
        self.update_customer_wallet_balance()

    def update_customer_wallet_balance(self):
        """Update the wallet balance on the Customer and active Membership."""
        # Calculate current balance from ledger
        total = frappe.db.sql(
            "SELECT SUM(amount) FROM `tabSalon Wallet` WHERE customer=%s AND docstatus=1",
            self.customer
        )[0][0] or 0
        
        # Update the specific membership record
        if self.membership:
            frappe.db.set_value('Customer Membership', self.membership, 'wallet_balance', total)
        
        # Also update on customer for quick access
        # frappe.db.set_value('Customer', self.customer, 'salon_wallet_balance', total)
