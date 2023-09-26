# See LICENSE file for full copyright and licensing details.
"""This Module Contain information related to freight Configuration."""

from odoo import _, api, fields, models
from odoo.exceptions import UserError
from datetime import datetime

class NewShipping(models.Model):
    """For New Shipment"""

    _name = "new.shipping"
    _description = "New Shipment"
    _inherit = ["portal.mixin", "mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Ship Name",default="New")
    country_id = fields.Many2one("res.country", string="Country")
    loading_port_id = fields.Many2one("freight.port", string="Loading Port")
    discharg_port_id = fields.Many2one("freight.port", string="Discharging Port")
    agent_id = fields.Many2one("res.partner", string="Agent")
    captain_id = fields.Many2one("res.partner", string="Captain")
    arrive_date = fields.Date(string="Arrive Date")
    is_quarentine = fields.Boolean(string="Is Quarentine", default=False)
    is_there_freight_prepaid = fields.Boolean(string="Is There Freight Prepaid", default=False)
    attachment = fields.Char(string='Attachments Link')

    @api.model
    def create(self, vals):
        res = super(NewShipping, self).create(vals)
        if vals and vals.get("country_id", False):
            seq = self.env["ir.sequence"].next_by_code("new.shipping")
            res.name = res.country_id.name + '-' + seq + '/' + str(datetime.today().year)
        return res

    def action_quarentine_bill(self):
        print("action")

    def action_freight_prepaid_bill(self):
        print("action")









   