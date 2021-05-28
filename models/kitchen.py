from odoo import models,fields,api

class KitchenProduct(models.Model):
    _name='kitchen.product'

    name=fields.Char(string='name')
    expiry=fields.Datetime(string='Expiry')
    weight=fields.Integer(string='Weight')
    count=fields.Integer(string='Count')
    is_refrigerated = fields.Boolean(string='Is Refrigerated')



