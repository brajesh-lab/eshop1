from asyncio import FastChildWatcher
from datetime import datetime
from distutils.archive_util import make_zipfile
from distutils.command.upload import upload
import email
from enum import unique
from operator import mod
from unicodedata import category, name
from django.db import models
import starlette

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 50)


    @staticmethod
    def get_ll_category():

        return Category.objects.all()
    
 

        


    def __str__(self):
        return self.name


class Item(models.Model):
    name     = models.CharField(max_length = 50)
    price    = models.PositiveIntegerField()
    img      = models.ImageField(upload_to = 'static/image')
    disc     = models.CharField (max_length = 100)
    category = models.ForeignKey(Category , on_delete = models.CASCADE)
     
    def __str__(self):
            return self.name
    

    @staticmethod
    def get_all_item():
        return Item.objects.all()
    
    @staticmethod
    def get_items_by_id(ids):
        return Item.objects.filter(id__in=ids)
    
    @staticmethod
     
    def get_items_byId(category_id):

        if category_id:
            return Item.objects.filter(category = category_id)
        else:
            return Item.objects.all()


class Customer(models.Model):
    f_name   = models.CharField(max_length = 30)
    l_name   = models.CharField(max_length = 20)
    email    = models.EmailField()
    phone    = models.CharField(max_length=10)
    password = models.CharField(max_length=20)


    def registers(self):
        self.save()
    
    def check_customer(self):
       if  Customer.objects.filter(email = self.email):
           return True
       else:
           False


    def check_phone(self):
        if  Customer.objects.filter(phone = self.phone):
           return True
        else:
           False
    @staticmethod
    def check_customer(email):
        try:
       
             return Customer.objects.get(email=email)
        except:
            return False
    def __str__(self):
            return self.f_name
    
class Order(models.Model):
    item     = models.ForeignKey(Item,on_delete=models.CASCADE)
    user     = models.ForeignKey(Customer, on_delete=models.CASCADE)
    add      = models.CharField(max_length=50 ,default = "")
    phone    = models.CharField(max_length=11)
    quantity = models.IntegerField(default=0)
    price    = models.IntegerField()
    date     = models.DateField(default=datetime.today)
    status   = models.BooleanField(default=False)



    def place_order(self):
        self.save()

    @staticmethod
    def  get_order_by_id(customer_id):
       return Order.objects.filter(user = customer_id)
        




    