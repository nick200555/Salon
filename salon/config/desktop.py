from frappe import _

def get_data():
    return [
        {
            "module_name": "Appointment Booking",
            "color": "#C0392B",
            "icon": "octicon octicon-calendar",
            "label": _("Appointment & Booking"),
            "type": "module",
        },
        {
            "module_name": "Salon Services",
            "color": "#8E44AD",
            "icon": "octicon octicon-star",
            "label": _("Salon Services & Treatments"),
            "type": "module",
        },
        {
            "module_name": "Membership Loyalty",
            "color": "#F1C40F",
            "icon": "octicon octicon-award",
            "label": _("Membership & Loyalty"),
            "type": "module",
        },
        {
            "module_name": "Inventory Management",
            "color": "#27AE60",
            "icon": "octicon octicon-package",
            "label": _("Inventory Management"),
            "type": "module",
        },
        {
            "module_name": "Customer Portal",
            "color": "#3498DB",
            "icon": "octicon octicon-globe",
            "label": _("Customer Portal Settings"),
            "type": "module",
        },
        {
            "module_name": "Reports Analytics",
            "color": "#34495E",
            "icon": "octicon octicon-graph",
            "label": _("Reports & Analytics"),
            "type": "module",
        },
    ]
