from odoo import _, api, fields, models
from datetime import datetime

class NewShipping(models.Model):
    """For New Shipment"""

    _name = "new.shipping"
    _description = "New Shipment"

    name = fields.Char(string="Shipment Name",default="New")
    shipname = fields.Char(string="Ship Name")
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
        if vals and vals.get("loading_port_id", False):
            seq = self.env["ir.sequence"].next_by_code("new.shipping")
            res.name = res.shipname + '_' + res.loading_port_id.code + '_' + seq + '/' + str(datetime.today().year)
        return res

    def action_quarentine_bill(self):
        print("action")
        
    def action_freight_prepaid_bill(self):
        print("action")

    def get_manifest(self):
        return {
            'name': 'Manifest',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'new.manifist',
            'target': 'current',
            'domain': [('shipping_id', '=', self.id)],
            'context': {'default_shipping_id': self.id, 'default_loading_port_id': self.loading_port_id.id,
                        'default_discharg_port_id': self.discharg_port_id.id, 'default_arrive_date':self.arrive_date}
        }

    def get_services(self):
        return {
            'name': '',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'wiz.invoice',
            'view_id': self.env.ref('scs_freight.wiz_customer_invoice_view').id,
            'target': 'new'
        }







   