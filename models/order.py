from odoo import models,fields,api
from odoo.exceptions import ValidationError

class RestaurantOrder(models.Model):
    _name="restaurant.order"

    dish=fields.Char(string='Dish')
    quantity=fields.Integer(string='Quantity')
    price=fields.Integer(string='Unit Price')
    total=fields.Integer(string='Total price')
    order_datetime=fields.Datetime(string='Order Date')
    waiter_id=fields.Char(string='Waiter Id')
    delivery_type=fields.Selection([('delivery','Delivery'),
                                    ('restro', 'Restro')])
    waiter_id=fields.Many2one('hotel.person','Waiters')
    domain=[('person_type','=','waiter')]
    state=fields.Selection([('new','New'),
                            ('kitchen','Kitchen'),
                            ('process','process'),
                            ('ready','Ready'),
                            ('delivered','Delivered'),
                            ('payment', 'Payment')])

    menu_id=fields.Many2one('food.menu','Menu')

    @api.model
    def create(self,vals):
        print('vals',vals)
        print('self',self)
        qty=vals.get('quantity',0)
        price=vals.get('price',0)
        vals.update({'total': qty*price})
        print('vals',vals)
        return super(RestaurantOrder, self).create(vals)


    def write(self,vals):
        print('self',self)
        #self is a recordset
        print('vals',vals)
        if vals.get('quantity',False) or vals.get('price'):
            print('entering if statement')
            qty=vals.get('quantity',False)
            print('quantity',qty)
            price=vals.get('price',False)
            print('price',price)
            if not qty:
                print('in if not qty')
                qty=self.quantity
            if not price:
                 print('in if not price')

                 price=self.price
            print('quantity',qty)
            print('price',price)
            vals.update({'total':qty*price})

        print(vals)
        return super(RestaurantOrder,self).write(vals)

    def unlink(self):
        print(self)
        for order in self:
            if order.state in ['ready','delivered','payment']:
                raise ValidationError('You cannot delete an order once it is\processed')

        return super(RestaurantOrder,self).unlink()

    def set_new(self):
        vals={'state':'new'}
        self.write(vals)
        return True
    def duplicate_order(self):
        print('self.waiter id',self.waiter_id)
        print('self.waiter_id.name',self.waiter_id.name)
        print('self.waiter_id.id',self.waiter_id.id)
        print('self.waiter_id.age',self.waiter_id.age)
        print('self.waiter_id.dob',self.waiter_id.dob)
        vals={'dish':self.dish,
              'price':self.price,
              'quantity':self.quantity,
              'total':self.total,
              'waiter_id': self.waiter_id.id,
              'state':self.state}
        res=self.create(vals)
        return res




















