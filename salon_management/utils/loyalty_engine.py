import frappe

def award_loyalty_points(doc, method=None):
    """Award loyalty points on Salon Appointment completion."""
    if doc.status != 'Completed':
        return
        
    cat = frappe.get_doc('Service Category', doc.service_category)
    
    # Get active membership for the customer
    membership = frappe.db.get_value('Customer Membership',
        {'customer': doc.customer, 'status': 'Active'},
        ['name', 'plan', 'loyalty_multiplier'], as_dict=True)
    
    multiplier = membership.loyalty_multiplier if membership else 1.0
    
    # Calculate points: category defaults * multiplier
    points = int(cat.loyalty_points_per_visit * multiplier)
    
    if points > 0:
        txn = frappe.new_doc('Loyalty Transaction')
        txn.customer = doc.customer
        txn.membership = membership.name if membership else None
        txn.transaction_type = 'Earn'
        txn.points = points
        txn.source_document = doc.name
        txn.notes = f'Points earned from appointment {doc.name}'
        txn.insert(ignore_permissions=True)
        # after_insert hook on Loyalty Transaction will update Customer balance

def update_customer_points_balance(doc, method=None):
    """Recalculate and cache loyalty_points_balance on Customer."""
    total = frappe.db.sql(
        "SELECT SUM(points) FROM `tabLoyalty Transaction` WHERE customer=%s", 
        doc.customer
    )[0][0] or 0
    
    frappe.db.set_value('Customer', doc.customer, 'loyalty_points_balance', int(total))
