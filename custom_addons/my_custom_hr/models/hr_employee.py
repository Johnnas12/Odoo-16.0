from odoo import models, fields

class HREmployee(models.Model):
    _inherit = 'hr.employee'

    custom_field = fields.Char(string="Custom Field")
