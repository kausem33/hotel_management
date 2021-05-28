from odoo import models,fields,api

class Person(models.Model):
    _name='hotel.person'

    name=fields.Char(string='person')
    age=fields.Integer(string='Age')
    weight=fields.Float(string='Weight')
    dob=fields.Date(string='date of birth')
    marital_status=fields.Boolean(string='Marital Staus')
    joining_date=fields.Datetime(string='Joining Date')
    orders=fields.One2many('restaurant.order','waiter_id',string='Order')
    person_type=fields.Selection([('customer','Customer'),
                                  ('waiter','Waiter'),
                                  ('chef','Chef')],default='waiter')

    chef_orders=fields.Many2many('restaurant.order',string='Chef_Orders')

