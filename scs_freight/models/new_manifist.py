# See LICENSE file for full copyright and licensing details.
"""This Module Contain information related to freight Configuration."""

from odoo import _, api, fields, models
from odoo.exceptions import UserError
from datetime import datetime
from odoo.exceptions import UserError, ValidationError
from lxml import etree

class NewManifist(models.Model):
    """For New Manifest"""

    _name = "new.manifist"
    _description = "New Manifist"
    _rec_name = "arrive_date"


    loading_port_id = fields.Many2one("freight.port", string="Port of Loading")
    discharg_port_id = fields.Many2one("freight.port", string="Port Of Discharge")
    arrive_date = fields.Date(string="Arrive Date")
    document_no = fields.Char(string="Document No")
    road_no = fields.Char(string="Road No")
    shipping_id = fields.Many2one("new.shipping",string="shipping")
    manifist_line_ids = fields.One2many(
        "new.manifist.line", "manifest_id", string="Order", copy=False
    )


    def my_button(self):
        return {
            'name': "Add Customer",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'wiz.customer.manifist',
            'view_id': self.env.ref('scs_freight.wiz_customer_manifiest_view').id,
            'target': 'new'
        }


    # @api.model
    # def create(self, vals):
    #     record = super(NewManifist, self).create(vals)
    #     found_manifest_ids = self.env['new.manifist'].search([('shipping_id', '=', record.shipping_id.id)])
    #     if len(found_manifest_ids) > 1:
    #         raise ValidationError(_('We Have alredy created a manifest for this shipment.'))
    #     return record

    # incomplete task
    # @api.model
    # def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
    #     res = super(NewManifist, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
    #     if view_type == 'tree':
    #         context = self.env.context
    #         print(">>>>>>>>>>>>>>>LLLLLLLLLLLLLLLLLL",context)
    #         if context.get('shipment_id'):
    #             found_manifest_ids = self.env['new.manifist'].search([('shipping_id', '=', context.get('shipment_id'))])
    #             if found_manifest_ids:
                    
    #                 doc = etree.XML(res['arch'])
    #                 for t in doc.xpath("//tree"):
    #                     t.attrib['create'] = 'false'
    #                 res['arch'] = etree.tostring(doc)
    #     return res
  

class NewManifistLine(models.Model):
    """For New Manifest"""

    _name = "new.manifist.line"
    _description = "New Manifist line"


    manifest_id = fields.Many2one("new.manifist", string="Manifist", copy=False)
    shipper_name = fields.Char(string="Shipper Name")
    consignee_name_id = fields.Many2one("res.partner", string="Consignee Name")
    total_no_of_contanier = fields.Char(string="Total Container")
    total_weight = fields.Char(string="Total Weight")
    total_package = fields.Char(string="Total Package")
    description = fields.Text(string="Description")
    final_port = fields.Many2one("freight.port", string="Final Port")
    marks_no = fields.Char(string="Marks No")
    container_no = fields.Char(string="container No")
    weight = fields.Float('Weight')
    no_packing = fields.Char('No Packing')
    tariff = fields.Char(string="Tariff")
    packages = fields.Char(string="Packages")


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

