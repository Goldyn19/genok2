from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from products.models import Cart_id, CartItem
from document.models import Credit_ID, CreditRecord

def fin_sec(request):
    if request.method == 'GET':
        cart_item = CartItem.objects.filter(cart_ID__is_checked_out=True, cart_ID__is_paid=False)
        template = loader.get_template('fin_sec.html')
        context = {
            'cart_item': cart_item
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
                    return redirect('fin_sec')
                elif value == 'credit':
                    return ('cart')
    template = loader.get_template('fin_sec.html')
    cart_item = CartItem.objects.filter(cart_ID__is_checked_out=True)
    context = {
        'cart_item': cart_item
    }
    return HttpResponse(template.render(context,request))



def secretary(request):
    template = loader.get_template('sec.html')
    context = {}
    return HttpResponse(template.render(context, request))




# Create your views here.