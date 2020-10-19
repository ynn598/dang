from django.urls import path

from cart import views

app_name="cart"

urlpatterns=[
    path("cart/",views.cart,name="cart"),
    path("add_cart/",views.add_cart,name="add_cart"),
    path("delete/",views.delete,name="delete"),
    path("exit/",views.exit,name="exit"),

]