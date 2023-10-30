from django.db import models
from django.db import models
from django.contrib.auth.models import User
from products.models import Cart_id, CartItem


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ChatMessage(models.Model):
    messageBody = models.CharField(max_length=500)
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='msg_sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='msg_receiver')
    seen = models.BooleanField(default=False)

    def __str__(self):
        return self.messageBody


class SystemMessages(models.Model):
    cartID = models.ForeignKey(Cart_id, on_delete=models.CASCADE)
    is_seen = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    is_collected = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)


# Create your models here.


# Create your models here.
