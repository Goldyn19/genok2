from django.db import models
from django.contrib.auth.models import User
import random


class Stock(models.Model):
    name = models.CharField(max_length=225, null=False)
    part_number = models.CharField(max_length=50, primary_key=True)
    location = models.CharField(max_length=10, null=False)
    balance = models.IntegerField()
    price = models.IntegerField(null=True)

    @property
    def Balance(self):
        return self.balance

    def __str__(self):
        return f"{self.name} {self.part_number} "


class Cart_id(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    cartID = models.CharField(max_length=50,)
    customer_name = models.CharField(max_length=50, null=False)
    is_checked_out = models.BooleanField(default=False)
    is_attended = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.customer_name}"


class CartItem(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cart_ID = models.ForeignKey(Cart_id, on_delete=models.CASCADE)


    @property
    def Price(self):
        return self.product.price

    def PartNumber(self):
        return self.product.part_number

    def PartName(self):
        return self.product.name

    def Total(self):
        return self.Price * self.quantity

    def AugmentedQuantity(self, quantity):
        self.quantity = self.quantity + int(quantity)
        self.save()

    def __str__(self):
        return f" {self.product.part_number} {self.product.name} "
    # {self.quantity} {self.price} {self.Total}


class Location(models.Model):
    location = models.CharField(max_length=5)


class SalesRecord(models.Model):
    item = models.ForeignKey(CartItem, on_delete=models.CASCADE)
    payment_method_choices = [
        ('Credit', 'Credit'),
        ('Paid', 'Paid')

    ]
    payment_method = models.CharField(
        max_length=6,
        choices=payment_method_choices,
    )
    is_confirmed = models.BooleanField(default=False)



# Create your models here.
