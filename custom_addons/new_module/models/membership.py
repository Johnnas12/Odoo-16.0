from odoo import models, fields

class GymMembership(models.Model):
   _name = "gym.membership"
   _inherit = ["mail.thread", "mail.activity.mixin"]
   _description = "Gym Membership"
   _rec_name = "reference"
   reference = fields.Char(string='GYM reference',required=True,readonly=True, default=lambda self: _('New'))
   member_id = fields.Many2one('res.partner', string='Member', required=True,tracking=True,
   domain="[('gym_member', '!=',False)]")
   membership_scheme_id = fields.Many2one('product.product',
                                       string='Membership scheme',
                                       required=True, tracking=True,
                                       domain="[('membership_date_from', '!=',False)]")
   paid_amount = fields.Integer(string="Paid Amount", tracking=True)
   membership_fees = fields.Float(string="Membership Fees", tracking=True,
                                  related="membership_scheme_id.list_price")
   sale_order_id = fields.Many2one('sale.order', string='Sales Order',
                                   ondelete='cascade', copy=False,
                                   readonly=True)
   membership_date_from = fields.Date(string='Membership Start Date',
                                      related="membership_scheme_id.membership_date_from",
                                      help='Date from which membership becomes active.')
   membership_date_to = fields.Date(string='Membership End Date',
                                    related="membership_scheme_id.membership_date_to",
                                    help='Date until which membership remains active.')
   company_id = fields.Many2one('res.company', string='Company', required=True, readonly=True,
                                default=lambda self: self.env.company)
