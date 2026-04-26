import frappe
from frappe.model.document import Document

class ProductUsageEntry(Document):
    def validate(self):
        self.total_items = len(self.products)
        self.calculate_total_cost()

    def calculate_total_cost(self):
        total = 0
        for p in self.products:
            if not p.valuation_rate:
                p.valuation_rate = frappe.db.get_value('Item', p.item, 'valuation_rate') or 0
            p.line_cost = (p.qty_used or 0) * (p.valuation_rate or 0)
            total += p.line_cost
        self.total_cost = total

    def on_submit(self):
        self.create_stock_entry_on_submit()
        self.update_session_product_cost()

    def on_cancel(self):
        self.cancel_stock_entry()

    def create_stock_entry_on_submit(self):
        """Creates ERPNext Stock Entry (Material Issue) from child table rows."""
        if self.stock_entry:
            return
            
        stock_entry = frappe.new_doc('Stock Entry')
        stock_entry.stock_entry_type = 'Material Issue'
        stock_entry.from_warehouse = self.branch # Assuming branch maps to warehouse
        stock_entry.posting_date = self.usage_date
        
        for p in self.products:
            stock_entry.append('items', {
                'item_code': p.item,
                'qty': p.qty_used,
                'uom': p.uom,
                'batch_no': p.batch_no,
                's_warehouse': self.branch
            })
            
        stock_entry.insert(ignore_permissions=True)
        stock_entry.submit()
        
        frappe.db.set_value('Product Usage Entry', self.name, {
            'stock_entry': stock_entry.name,
            'status': 'Stock Deducted'
        })

    def cancel_stock_entry(self):
        if self.stock_entry:
            se = frappe.get_doc('Stock Entry', self.stock_entry)
            if se.docstatus == 1:
                se.cancel()

    def update_session_product_cost(self):
        if self.service_session:
            # logic to update total product cost on the linked Service Session
            pass
