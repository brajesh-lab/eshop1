from atexit import register
from django import template
from sqlalchemy import false

register = template.Library()

@register.filter(name = 'is_in_cart')
def is_in_cart(items,cart):
    key  = cart.keys()
    for id in key:
        if int(id) == items.id:
             return True;
       

    return False;
    

  
  

@register.filter(name = 'count')
def count(items,cart):
    key  = cart.keys()
    for id in key:
        if int(id) == items.id:
            return cart.get(id)

  
    return 0
    
  

@register.filter(name = 'total_price')
def total_price(items,cart):
    return items.price*count(items,cart)

@register.filter(name = 'total_cart_price')
def total_cart_price(items,cart):
    sum=0
    for p in items:
        sum+= total_price(p,cart)
    
    return sum

@register.filter(name = 'currency')
def currency(number):
    return "₹ "+str(number)

@register.filter(name = 'order_price')
def order_price(price,quntity):
    return price*quntity

@register.filter(name = 'order_total_price')
def order_total_price(price,quntity):
    return price*quntity



   