from django.db import models
from products.models import *


class PurchaseBook(models.Model):
    part_number = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity_in = models.IntegerField(default=0)
    location = models.CharField(max_length=5)
    price = models.IntegerField(null=True)
    date_added = models.DateField(auto_now_add=True, null=True)


class Credit_ID(models.Model):
    customer_name = models.CharField(max_length=125)
    customer_id = models.CharField(max_length=50)


class CreditRecord(models.Model):
    item = models.ForeignKey(Cart_id, on_delete=models.CASCADE, null=True)
    amount_paid = models.IntegerField(default=0)
    credit = models.IntegerField(default=0)
    customer = models.ForeignKey(Credit_ID, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True, null=True)



# Create your models here.

# Create your models here.
