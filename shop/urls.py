from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('about/', views.AboutUs, name="AboutUs"),
    path('contact/', views.ContactUs, name="ContactUs"),
    path('tracker/', views.Tracker, name="Tracker"),
    path('cart/', views.Cart, name="Cart"),
    path('search/', views.Search, name="Search"),
    path('products/<int:pid>', views.ProductView, name="ProductView"),
    path('checkout/', views.CheckOut, name="CheckOut"),
    path('payment/', views.Payment, name="Payment"),
    path('handlerequest/', views.handlerequest, name="HandleRequest"),
]