from datetime import date, datetime
from email import message
from os import remove
from turtle import pos
from unicodedata import name
from MySQLdb import Date
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from numpy import product
from sqlalchemy import null
from.models import Customer, Item,Category, Order

# Create your views here.
def index(request):
  
    #add To Cart........................................................................
    if request.method == 'POST'    :
        items = request.POST.get("id")
        remove  = request.POST.get('remove')
        cart    = request.session.get('cart')
       
        
        


        if cart:
            quantity      =  cart.get(items)
            print("qqq",quantity)
            if quantity:
               
                if not remove:
                    cart[items] = quantity+1
                    
                    
                    
                  
                else:
                    print('remove block',cart[items],'=',quantity)
                    if quantity <=1:
                        cart.pop(items)
                        print("pop suceesfully")
                    else:

                       cart[items] = quantity-1

                     
            else:
                cart[items] = 1
        
        else :
            cart          = {}
            cart[items] = 1

        request.session['cart'] = cart
       
    #....................................................................................
    items    = None
    cart =  request.session.get('cart')
    
    if not cart:
        request.session['cart'] = {}
    category = Category.get_ll_category()
  
    categoryid = request.GET.get('category')
    
    if categoryid:
        items = Item.get_items_byId(categoryid)
    else:
        items = Item.get_all_item()
   
    data             = {}
    data['item']     = items
    data['category'] = category


    return render(request ,'index1.html', data)

def signup(request):

    if request.method == 'GET':
         return render(request, 'signup.html')
    
    else:
        postdata = request.POST
        f_name   = postdata.get('f_name')
        l_name   = postdata.get('L_name')
        email    = postdata.get('email')
        phone    = postdata.get('phone')
        password = postdata.get('password')
        

        val      = {'f_name' : f_name, 'l_name' :l_name ,
                     'email' : email ,'phone' : phone }

        customer = Customer(f_name = f_name, l_name = l_name , 
                     email = email ,phone = phone  ,password = password)

        #validation----------------------
        import re
        error = ""
        if not f_name:
            error = 'First name required'
           
        elif  not l_name:
             
            error = 'Last name required'
            
        elif not email:
            error = "email must be required !!"

        elif not phone:
            error = 'phone number is required'
        elif  len(phone)< 10:
              error = 'phone number must be 10 digit !!!'

        elif not re.findall('[a-z]',password):
            error = "one lower case required in password!!!"
        elif not re.findall('[A-Z]',password):
            error = " at least one Upper case Required in password !!!"
        elif not re.findall("[0-9]",password):
            error = "at least one number required in password!!"
        elif not re.findall("[^a-zA-Z0-9]",password):
            error = 'at least one special character required in password!!!'
        elif customer.check_customer(email):
            error = "email all ready registered"
        elif customer.check_phone():
            error = "phone number is registered"

         

    
        if not error:

            message  = "Account created successfully"

            customer.password = make_password(customer.password)
            customer.registers()
            return render(request,'signup.html',{'msg':message})
        else:
            data = {'error':error,'val':val}
            
            return render(request,'signup.html',data)


def login(request):
    error     = ""
    if request.method == 'POST':

        
       
        email   = request.POST.get('email')
        
        password  = request.POST.get('password')

        user     = Customer.check_customer(email)

       
         
        if user:
            flag = check_password(password, user.password)
            print(flag)
            if flag:
                request.session['user_id']    = user.id 
                request.session['user_email'] = user.email
               
            
                
                return redirect('index1')
            else:
                error = "Wrong Password !!!!"
        else:
            error = "User not registered !!!"

    return render(request, "login.html",{'error':error})

def logout(request):
    request.session.clear()
    return redirect('index1')

def cart(request):

    cart =  request.session.get('cart')
    
    if not cart:
        request.session['cart'] = {}
    data ={}
    item = ''
    items    = None
    dict = request.session.get('cart')
    print("dic",dict)
    lists  =list(dict.keys())
    
   
    
    
    if request.method == 'POST'    :
        items = request.POST.get("id")
        remove  = request.POST.get('remove')
        cart    = request.session.get('cart')
        item = Item.get_items_by_id(items)
       
        data['item']= item
        if cart:
            quantity      =  cart.get(items)
            
            if quantity:
               
                if not remove:
                    cart[items] = quantity+1
                    
                    
                    
                  
                else:
                    print('remove block',cart[items],'=',quantity)
                    if quantity <=1:
                        cart.pop(items)
                        print("pop suceesfully")
                    else:

                       cart[items] = quantity-1

                     
            else:
                cart[items] = 1
        
        else :
            cart          = {}
            cart[items] = 1

        request.session['cart'] = cart
        print("items",items)
    #....................................................................................
    print(lists)
    for id in lists:
        print("list",lists)
        if id == items:
            lists.remove(id)
        
    print("list=",lists)

    items=Item.get_items_by_id(lists)
    data['items'] =  items

    

    return render(request,'cart.html',data)

def checkout(request):
    if request.method =="POST":
       add   = request.POST.get('Address')
       phone = request.POST.get('Phone')
       user  = request.session.get('user_id')
       cart  = request.session.get('cart')
       items = Item.get_items_by_id(list(cart.keys()))
       
      
       for item in items:
          order = Order(item = item, user = Customer(id=user), add = add ,phone = phone, quantity  = cart.get(str(item.id)),price = item.price)
          order.place_order()
       request.session['cart'] = {}
      

    return redirect('cart')

def order(request):
    if request.method ==  'GET':
          user   = request.session.get('user_id')
          
          orders = Order.get_order_by_id(user)
          print(orders)
  
    return render(request,'order.html',{'orders':orders})

  
   



       
        
        


        
                    
                  
               
        
    