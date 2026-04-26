frappe.ui.form.on('Salon Appointment', {
	setup: function(frm) {
		frm.set_query('primary_stylist', function() {
			return {
				filters: {
					'designation': ['in', ['Stylist', 'Therapist', 'Senior Stylist']]
				}
			};
		});
	},
	refresh: function(frm) {
		if (frm.doc.docstatus === 1 && frm.doc.status === 'Completed' && !frm.doc.pos_invoice) {
			frm.add_custom_button(__('Create Invoice'), function() {
				frm.call('create_pos_invoice_on_completion');
			});
		}
	},
	customer: function(frm) {
		if (frm.doc.customer) {
			frappe.db.get_value('Customer', frm.doc.customer, 'preferred_stylist', (r) => {
				if (r.preferred_stylist) {
					frm.set_value('primary_stylist', r.preferred_stylist);
				}
			});
		}
	},
    appointment_date: function(frm) {
        if (frm.doc.appointment_date && frm.doc.branch && frm.doc.service_category) {
            frm.trigger('get_available_slots');
        }
    },
    get_available_slots: function(frm) {
        frappe.call({
            method: 'salon_management.utils.slot_engine.get_open_slots',
            args: {
                branch: frm.doc.branch,
                service_category: frm.doc.service_category,
                appointment_date: frm.doc.appointment_date
            },
            callback: function(r) {
                if (r.message) {
                    // logic to show slots in UI or console
                }
            }
        });
    }
});
