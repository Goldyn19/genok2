from .models import Stock, CartItem
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
import decimal
import random
import inflect


def _generate_cart_id():
    cart_id = ''
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
    cart_id_lenght = 49
    for y in range(cart_id_lenght):
        cart_id += characters[random.randint(0, len(characters)-1)]
    return cart_id


def get_cart_items(request):
    return CartItem.objects.filter(cart_id=_generate_cart_id(request))


def convert_digit_to_word(digit):
    p = inflect.engine()
    word = p.number_to_words(digit)
    return word

def generate_credit_id():
    credit_id = ''
    characters = 'abcdefghijklmnopqrstuvwxyz1234567890'
    credit_id_lenght = 20
    for y in range(credit_id_lenght):
        credit_id += characters[random.randint(0, len(characters)-1)]
    return credit_id
# return CartItem.objects.filter(cart_id = _cart_id(request))





