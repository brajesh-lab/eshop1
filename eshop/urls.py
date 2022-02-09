"""eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import imp
from unicodedata import name
from django.contrib import admin
from django.urls import path
from store import views
from django.conf.urls.static import static
from . import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index1'),
    path('signup', views.signup, name = 'signup'),
    path('login',views.login),
    path('logout',views.logout, name='logout'),
    path('cart',views.cart,name='cart'),
    path('checkout',views.checkout, name="checkout"),
    path('order',views.order, name='order'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)