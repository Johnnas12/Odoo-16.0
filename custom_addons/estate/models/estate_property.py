from odoo import  models, fields
from datetime import timedelta, date


class EstateProperty(models.Model):
    # Definition of model name and description for model
    _name = 'estate.property'
    _description = 'model for real estate property'

    # The below are table columns of table name estate_property
    name = fields.Char(string="Name",  required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string="Date Availability", copy=False, default= lambda self: self._default_date_availability())
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(string='Selling Price', readonly=True, copy=False)
    bedrooms = fields.Integer(string='Bedrooms', default=2)
    living_area = fields.Integer(string='Living Area')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string= 'Garden Area')
    garden_orientation = fields.Selection(string='Garden Orientation',
                                          selection=[
                                                    ('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West'),
                                                    ])
    state = fields.Selection(string='State', selection=[('new', 'New'), ('offer recieved', 'Offer Recieved'), ('offer accepted', 'Offer Accepted'), ('cancelled', 'Cancelled')])
    active = fields.Boolean(default= True)


    def _default_date_availability(self):
        return date.today() + timedelta(days=90)

    def copy(self, default = None):
        default = dict(default or {})

        default['date_availability'] = self._default_date_availability()
        default['selling_price'] = 0

        return super(EstateProperty, self).copy(default)