from odoo import models, fields, api, _

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _inherit = 'mail.thread'
    _description = "Doctors Records"
    # _rec_name = 'ref'

    name = fields.Char(string='Name', required=True, tracking=True)
    gender = fields.Selection([('male', "Male"), ('female', 'Female')], string='Gender',  required=True, tracking=True)
    ref = fields.Char(string='Reference', required=True)
    active = fields.Boolean(default= True)

    def name_get(self):
        res= []
        for rec in self:
            name= f'{rec.ref} - {rec.name}'
            res.append((rec.id, name))
        return res
