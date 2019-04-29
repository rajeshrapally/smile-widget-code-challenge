from django.urls import path, include
from . import views 

urlpatterns =[
    #Get product price by passing productcode, date and giftCardCode 
    path('get-price/',views.getprice,name="get-price"),

]