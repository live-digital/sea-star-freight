from odoo import _, api, fields, models
from datetime import datetime

class NewShipping(models.Model):
    """For New Shipment"""

    _name = "new.shipping"
    _description = "New Shipment"

    name = fields.Char(string="Shipment Name")
    shipname_id = fields.Many2one("freight.vessels", string="Ship Name")
    country_id = fields.Many2one("res.country", string="Country")
    loading_port_id = fields.Many2one("freight.port", string="Loading Port")
    discharg_port_id = fields.Many2one("freight.port", string="Discharging Port")
    agent_id = fields.Many2one("res.partner", string="Agent",domain="[('agent', '=', True)]")
    captain = fields.Char(string="Captain")
    arrive_date = fields.Date(string="Arrive Date")
    is_quarantine = fields.Boolean(string="Is Quarantine", default=False)
    is_there_freight_prepaid = fields.Boolean(string="Is Freight Prepaid", default=False)
    attachment = fields.Char(string='Attachments Link')

    @api.model
    def create(self, vals):
        res = super(NewShipping, self).create(vals)
        if vals and vals.get("loading_port_id", False):
            seq = self.env["ir.sequence"].next_by_code("new.shipping")
            res.name = res.shipname_id.name + '_' + res.loading_port_id.code + '_' + seq + '/' + str(datetime.today().year)
        return res

    def action_quarentine_bill(self):
        print("action")
        
    def action_freight_prepaid_bill(self):
        print("action")

    # @api.onchange('agent_id')
    # def _onchange_captain(self):
    #     print(">>>>>>>>>>>???????????????????????_onchange_captain")
    #     sale_order = self.env['sale.order'].search([('state','in',['sale','sent'])])
    #     print(">>>>>>>>>>>???????????????????????_onchange_captain",sale_order)
    #     for rec in self:
    #         rec.capt = 'shiva'


        # self.delivery_message = False
        # if self.delivery_type in ('fixed', 'base_on_rule'):
        #     vals = self._get_shipment_rate()
        #     if vals.get('error_message'):
        #         return {'error': vals['error_message']}
        # else:
        #     self.display_price = 0
        #     self.delivery_price = 0

    def get_manifest(self):
        context = {'default_shipping_id': self.id, 'default_loading_port_id': self.loading_port_id.id,
                        'default_discharg_port_id': self.discharg_port_id.id, 'default_arrive_date':self.arrive_date,'shipment_id':self.id}
        manifest = self.env['new.manifist'].sudo().search([('shipping_id','=',self.id)])
        if manifest:
            context['create'] = False
        return {
            'name': 'Manifest',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'new.manifist',
            'target': 'current',
            'domain': [('shipping_id', '=', self.id)],
            'context': context
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







   