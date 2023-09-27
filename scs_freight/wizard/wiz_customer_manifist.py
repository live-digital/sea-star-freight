# See LICENSE file for full copyright and licensing details.
"""Model for the track operation."""

from odoo import _, fields, models
from odoo.exceptions import UserError


class WizCustomerManifist(models.TransientModel):
    """Transient Model for track Record."""

    _name = "wiz.customer.manifist"
    _description = "Wiz Customer Manifist"

    shipper_name = fields.Char(string="Shipper Name")
    consignee_name = fields.Char(string="Consignee Name")
    total_no_of_contanier = fields.Char(string="Total Container")
    total_weight = fields.Char(string="Total Weight")
    total_package = fields.Char(string="Total Package")
    discription = fields.Char(string="Discription")
    consignee_name = fields.Char(string="Consignee Name")
    final_port = fields.Many2one("freight.port", string="Final Port")
   
    def action_done(self):
        print("shivaaaaaaaaaaa")
        active_id = self._context.get('active_id')
        record_id = self.env['new.manifist'].browse(active_id)
        vals = {'shipper_name': self.shipper_name,
                'consignee_name' : self.consignee_name,
                'total_no_of_contanier': self.total_no_of_contanier,
                'total_weight' : self.total_weight,
                'total_package' : self.total_package,
                'final_port' : self.final_port.id,}
        record_id.update({'manifist_line_ids': [(0,0,vals)]})



class WizInvoice(models.TransientModel):
    """Transient Model for track Record."""

    _name = "wiz.invoice"
    _description = "Wiz invoice"


    def action_done(self):
        print("shivaaaaaaaaaaa")

class WizLineInvoice(models.TransientModel):
    """Transient Model for track Record."""

    _name = "wiz.line.invoice"
    _description = "Wiz Line Invoice"


    def delivery_permit_invoice(self):
        print("shivaaaaaaaaaaa")

    def freight_prepaid_invoice(self):
        print("shivaaaaaaaaaaa")

    def Quarantine_invoice(self):
        print("shivaaaaaaaaaaa")