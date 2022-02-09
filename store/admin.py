from django.contrib import admin
from .models import  Item,Category,Customer, Order
# Register your models here.


class Categorys(admin.ModelAdmin):

    
    list_display =  ['name']
admin.site.register(Category, Categorys)


class Product(admin.ModelAdmin):
    list_display = ['name','price','img','disc','category']


admin.site.register(Item,Product)

class Customers(admin.ModelAdmin):
    list_display = ['f_name','l_name','email','phone','password']

admin.site.register(Customer,Customers)

class order(admin.ModelAdmin):
    list_display = ['item','user','quantity','price','date']

admin.site.register(Order,order)