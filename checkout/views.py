from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

from products.cart import convert_digit_to_word
from products.models import Cart_id, CartItem, SalesRecord
from document.models import Credit_ID, CreditRecord


def fin_sec(request):
    if request.method == 'GET':
        cart_item = CartItem.objects.filter(cart_ID__is_checked_out=True, cart_ID__is_paid=False)

        template = loader.get_template('fin_sec.html')
        context = {
            'cart_item': cart_item,

        }
        return HttpResponse(template.render(context, request))
    elif request.method == 'POST':
        cart_id = request.POST['cart_id']
        for x in request.POST:
            if x == 'radio':
                value = request.POST['radio']
                if value == 'paid':
                    cartID = get_object_or_404(Cart_id, cartID=cart_id)
                    cartID.is_paid = True
                    cartID.save()
                    cart_item = CartItem.object.filter(cart_ID=cartID)
                    for items in cart_item:
                        sales_record = SalesRecord(item=items, payment_method='Paid', is_confirmed=False)
                        sales_record.save()
                    return redirect('fin_sec')
                elif value == 'credit':
                    cartID = get_object_or_404(Cart_id, cartID=cart_id)
                    customer_credit = request.POST['customer_credit']
                    cartID.is_paid = True
                    cartID.save()
                    cart_item = CartItem.object.filter(cart_ID=cartID)
                    for items in cart_item:
                        sales_record = SalesRecord(item=items, payment_method='Credit', is_confirmed=False)
                        sales_record.save()
                        credit_record = CreditRecord()
                    return ('cart')
    template = loader.get_template('fin_sec.html')
    cart_item = CartItem.objects.filter(cart_ID__is_checked_out=True)
    context = {
        'cart_item': cart_item
    }
    return HttpResponse(template.render(context,request))


def confirm_checkout(request, cart_id):
    cartID = get_object_or_404(Cart_id, cartID=cart_id)
    cart = CartItem.objects.filter(cart_ID=cartID)
    total = sum(item.Total() for item in cart)
    credit_id = Credit_ID.objects.all()
    total_words = convert_digit_to_word(total)
    template = loader.get_template('confirm_checkout.html')
    context = {
        'cart':cart,
        'total': total,
        'total_words': total_words,
        'credit_id': credit_id,
    }
    return HttpResponse(template.render(context, request))




# Create your views here.