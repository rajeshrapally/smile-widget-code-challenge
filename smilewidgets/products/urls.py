from django.urls import path, include
from . import views 

urlpatterns =[
    #Get product price by passing productcode, date and giftCardCode 
    path('get-price/<str:productCode>/<str:date>/',views.getprice,name="get-price"),

]