from django.db import models
from django.db.models import Q

def format_amount(amount):
    """fn used for format amount from cents to $ and appending $symbol"""
    return '${0:.2f}'.format(amount / 100)

class Product(models.Model):
    name = models.CharField(max_length=25, help_text='Customer facing name of product')
    code = models.CharField(max_length=10, help_text='Internal facing reference to product')
    price = models.PositiveIntegerField(help_text='Price of product in cents')
    
    def __str__(self):
        return '{} - {}'.format(self.name, self.code)

    def get_special_price(self,date):
        productprice_object = ProductPrice.objects.filter(product=self,date_start__lte=date).filter(Q(date_end__isnull=True)|Q(date_end__gte=date)).order_by('-price').first()
        if productprice_object:
            return productprice_object.price
        else:
            return self.price

class GiftCard(models.Model):
    code = models.CharField(max_length=30)
    amount = models.PositiveIntegerField(help_text='Value of gift card in cents')
    date_start = models.DateField()
    date_end = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return '{} - {}'.format(self.code, self.formatted_amount)
    
    @property
    def formatted_amount(self):
        return '${0:.2f}'.format(self.amount / 100)

class ProductPrice(models.Model):
    """ This model is used for schedule the offers on special days """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text='Description for the discounted Price')
    price = models.PositiveIntegerField(help_text='Discounted Price of product in cents')
    date_start = models.DateField()
    date_end = models.DateField(blank=True, null=True)

    def __str__(self):
        return 'Actual Price:{} - discounted Price:{}, your savings: {}'.format(format_amount(self.product.price),
                     format_amount(self.price), format_amount(self.product.price - self.price))
    
