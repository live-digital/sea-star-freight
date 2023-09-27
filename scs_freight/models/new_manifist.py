# See LICENSE file for full copyright and licensing details.
"""This Module Contain information related to freight Configuration."""

from odoo import _, api, fields, models
from odoo.exceptions import UserError
from datetime import datetime

class NewManifist(models.Model):
    """For New Manifest"""

    _name = "new.manifist"
    _description = "New Manifist"
    _rec_name = "arrive_date"


    loading_port_id = fields.Many2one("freight.port", string="Port of Loading")
    discharg_port_id = fields.Many2one("freight.port", string="Port Of Discharge")
    arrive_date = fields.Date(string="Arrive Date")
    shipping_id = fields.Many2one("new.shipping",string="shipping")
    manifist_line_ids = fields.One2many(
        "new.manifist.line", "manifest_id", string="Order", copy=False
    )


    def my_button(self):
        print("shivaaaaaaaaaaaaaaaaaaaa")
        return {
            'name': "Add Customer",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'wiz.customer.manifist',
            'view_id': self.env.ref('scs_freight.wiz_customer_manifiest_view').id,
            'target': 'new'
        }


class NewManifistLine(models.Model):
    """For New Manifest"""

    _name = "new.manifist.line"
    _description = "New Manifist line"


    manifest_id = fields.Many2one("new.manifist", string="Manifist", copy=False)
    shipper_name = fields.Char(string="Shipper Name")
    consignee_name = fields.Char(string="Consignee Name")
    total_no_of_contanier = fields.Char(string="Total Container")
    total_weight = fields.Char(string="Total Weight")
    total_package = fields.Char(string="Total Package")
    description = fields.Text(string="Description")
    consignee_name = fields.Char(string="Consignee Name")
    final_port = fields.Many2one("freight.port", string="Final Port")

    def my_invoicing(self):
        return {
            'name': '',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'wiz.line.invoice',
            'view_id': self.env.ref('scs_freight.wiz_line_invoice_view').id,
            'target': 'new'
        }

