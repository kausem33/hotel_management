from odoo import models,fields,api
class FoodMenu(models.Model):
    _name='food.menu'

    name=fields.Char(string='Dishname')
    price=fields.Integer(string='Price')

