from django.shortcuts import render
from .models import Product,ProductPrice,GiftCard,format_amount
from datetime import datetime
from django.http import JsonResponse

def getprice(request, productCode, date):
    giftCardCode = request.GET.get('giftCardCode')
    success = False
    response = {}
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
        product_object = Product.objects.get(code=productCode)
        product_price = product_object.get_special_price(date) #checks and return the specialprice if available in the current date else return price
        if giftCardCode: #optional if giftCardCode passed in the url this block executes
            try:            
                giftcard_object = GiftCard.objects.get(code=giftCardCode,date_start__lte=date,date_end__gte=date)
                product_price = product_price-giftcard_object.amount #gift card amount applied to price
            except:
                response['message'] = "Invalid code or the giftCardCode is expired" #if the giftCardCode is wrong or not available in the start and end dates
        if product_price < 1:
            response['price'] = "Free"
        else:
            response['price'] = format_amount(product_price) #format amount
        success = True
    except Exception as e:
        response['message'] = str(e)


    return JsonResponse({
        'success' : success,
        'data' : response
        })
