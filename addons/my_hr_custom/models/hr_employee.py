from odoo import  models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    new_field = fields.Char("New Custom Field")
