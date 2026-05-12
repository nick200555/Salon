import frappe
from frappe import _

def get_data():
	return {}

def get_onboarding_data():
	return {
		"title": _("Welcome to Salon"),
		"subtitle": _("Complete these steps to setup your salon."),
		"success_message": _("You are all set to manage your salon!"),
		"docs_url": "",
		"items": [
			{
				"title": _("Create a Membership Plan"),
				"description": _("Define membership plans and their benefits."),
				"route": ["List", "Membership Plan"],
			},
			{
				"title": _("Set up Salon Services"),
				"description": _("Add the services you offer in your salon."),
				"route": ["List", "Service Item"],
			},
			{
				"title": _("Configure Salon Settings"),
				"description": _("Configure basic settings for your salon."),
				"route": ["Form", "Salon Management Settings"],
			}
		]
	}
