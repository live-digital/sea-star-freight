# See LICENSE file for full copyright and licensing details.

{
    # Module Info.
    "name": "Sea Star",
    "version": "14.0.2.0.1",
    "sequence": 1,
    "category": "Transport",
    "license": "LGPL-3",
    "summary": """Freight Management System for Carriers, Transport,
                  Goods Import/Export, Shipping and
                  Transportation Solutions,
                  Freight Management Software.""",
    "description": """
		    This module helps you to manage all freight operations by Air, Ocean, and Land.it is a comprehensive system to manage all aspects of your freight operations.
			Freight Management System		    
			freight management
			freight management system
			freight management software
			freight management services
			freight management solutions
			freight management companies
			freight maintenance management
			freight invoice management
			best freight management software
			best software for freight management
			freight rate management software
			Freight Transport Management
			Transport Management
			freight systemcarriers
			Freight Management System for Carriers
			Transport
			Goods Import/Export
			SCS Freight Management
			Shipping and Transportation Solutions
			freight management software
			freight transport
			goods import-export
			transportation solutions
			transportation management
			freight module
			Freight Transport
			Odoo freight management
			odoo freight 
			management
			freight
			""",         
			                    
    # Author
    "author": "Serpent Consulting Services Pvt. Ltd.",
    "website": "http://www.serpentcs.com",
    "maintainer": "Serpent Consulting Services Pvt. Ltd.",
    
    # Dependencies
    "depends": ["product", "account"],
    
    # Data
    "data": [
        "security/freight_security.xml",
        "security/ir.model.access.csv",
        "data/ir_sequence_data.xml",
        "data/mail_template.xml",
        "views/operation_service_view.xml",
        "views/freight_invoices_bills_views.xml",
        "views/freight_operation_view.xml",
        "views/new_shipping.xml",
        "wizard/wiz_order_track_view.xml",
        "wizard/wiz_custom_revision_reason_view.xml",
        "wizard/wiz_set_shipping_date_view.xml",
        "views/freight_custom_clearance_view.xml",
        "views/freight_config.xml",
        "views/res_partner.xml",
        "views/product.xml",
        "views/operation_tracking_view.xml",
        "report/shipping_analysis.xml",
        "report/shipping_order.xml",
        "report/payment_receipt_report_view.xml",
        "report/report_registration.xml",
    ],
    
    # Odoo App Store Specific
    "images": ["static/description/freight_banner.png"],
    "live_test_url": "https://www.youtube.com/watch?v=_P1Q4aoU9_0&list=PL4Wugt3LKrSS5tqr0gPwekhPNnYhJGHye",
    
    # Technical
    
    "application": True,
    "installable": True,
    "price": 80,
    "currency": "EUR",
}
