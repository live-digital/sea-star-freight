"""Inherited Res Partner Model."""
# See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResPartner(models.Model):
    """Inherit Partner Model."""

    _inherit = "res.partner"

    agent = fields.Boolean(string="Is Agent?")
    shipper = fields.Boolean(string="Is Shipper?")
    name_2 = fields.Char(string="Name 2")


