from django.contrib import admin
from django.urls import path
from warranty import views

urlpatterns = [
    path('',views.index,name='signin'),
    path('inventory',views.inventory,name='inventory'),
    path('home',views.home,name='home'),
    path('additem',views.additem,name='additem'),
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('signout',views.signout,name='signout'),
    path('search',views.search,name="search")
]