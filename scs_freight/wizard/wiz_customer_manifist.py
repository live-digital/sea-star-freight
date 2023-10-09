# See LICENSE file for full copyright and licensing details.
"""Model for the track operation."""

from odoo import _, fields, models
from odoo.exceptions import UserError


class WizCustomerManifist(models.TransientModel):
    """Transient Model for track Record."""

    _name = "wiz.customer.manifist"
    _description = "Wiz Customer Manifist"

    shipper_name = fields.Many2one("res.partner", string="Shipper Name",domain="[('shipper', '=', True)]")
    marks_no = fields.Char(string="Marks No")
    container_no = fields.Char(string="container No")
    consignee_name_id = fields.Many2one("res.partner", string="Consignee Name")
    total_no_of_contanier = fields.Char(string="Total Container")
    total_weight = fields.Char(string="Total Weight")
    total_package = fields.Char(string="Total Package")
    weight = fields.Float('Weight')
    no_packing = fields.Char('No Packing')
    description = fields.Char(string="Description" ,default="Sheeps")
    description_arabic = fields.Char(string="Description Arabic",default="ضأن")
    tariff = fields.Char(string="Tariff",default="Sheep")
    tariff_arabic = fields.Char(string="Tariff Arabic",default="الأغنام")
    final_port = fields.Many2one("freight.port", string="Final Port")
    packages = fields.Char(string="Package Type",default="Unit")
    packages_arabic = fields.Char(string="Package Type Arabic",default="وحدة")
   
    def action_done(self):
        active_id = self._context.get('active_id')
        record_id = self.env['new.manifist'].browse(active_id)
        vals = {'shipper_name': self.shipper_name.name,
                'total_no_of_contanier': self.total_no_of_contanier,
                'total_weight' : self.total_weight,
                'total_package' : self.total_package,
                'final_port' : self.final_port.id,
                'consignee_name_id' : self.consignee_name_id.id,
                'description' : self.description,
                'marks_no': self.marks_no,
                'container_no' : self.container_no,
                'weight' : self.weight,
                'no_packing' : self.no_packing,
                'tariff' : self.tariff,
                'packages' : self.packages,}
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
