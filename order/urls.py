from django.urls import path
from order import views

app_name = "order"

urlpatterns=[
    path("indent/",views.indent,name="indent"),
    path("indent_ok/",views.indent_ok,name="indent_ok"),
    path("address_logic/",views.address_logic,name="address_logic"),
    path("auto_address/",views.auto_address,name="auto_address"),
]