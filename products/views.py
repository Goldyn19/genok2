from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Stock, CartItem, Cart_id
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .cart import _generate_cart_id, convert_digit_to_word
#from chat.models import SystemMessages


@login_required(login_url='login_user')
def dashboard(request):
    stock = Stock.objects.all()
    user = request.user.username
    paginator = Paginator(stock, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = loader.get_template('dashboard.html')
    context = {
        'stock': stock,
        'page_obj': page_obj,
        'username': user
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='login_user')
def Carts(request):
    if request.method == 'POST':
        for x in request.POST:
            if x == 'customer_name':
                customer_name = request.POST['customer_name']
                user = request.user.username
                user_id = get_object_or_404(User, username=user)
                cart_id = _generate_cart_id()
                cartid = Cart_id(cartID=cart_id, userID=user_id, customer_name=customer_name)
                cartid.save()
                return redirect('create_cart', cart_id)
            elif x == 'customer_name2':
                cart_ID = request.POST['customer_name2']
                return redirect('view_cart_details',cart_ID)

    else:
        user = request.user.username
        user_id = get_object_or_404(User, username=user)
        cart_id = Cart_id.objects.filter(userID=user_id)
        cart_items = CartItem.objects.filter(userID=user_id, cart_ID__is_checked_out = False)
        template = loader.get_template('cart.html')
        context = {
            'cart_items': cart_items,
            'username': user,
            'cart_id': cart_id,
        }
        return HttpResponse(template.render(context, request))


@login_required(login_url='login_user')
def Create_cart(request, cart_id):
    if request.method == 'POST':
        part_number = request.POST['part_number']
        cart_id = cart_id
        quantity = request.POST['quantity']
        user = request.user.username
        user_id = get_object_or_404(User, username=user)
        return redirect('add_to_cart',cart_id, part_number, quantity)
    else:
        stock = Stock.objects.all()
        user = request.user.username
        cart_id = cart_id
        customer = get_object_or_404(Cart_id, cartID=cart_id)
        customer_name = customer.customer_name
        user_id = get_object_or_404(User, username=user)
        template = loader.get_template('customer_cart.html')
        context = {
            'stock': stock,
            'customer_name': customer_name,
            'username': user,
            'cart_id' : cart_id

        }
        return HttpResponse(template.render(context, request))


@login_required(login_url='login_user')
def View_cart_details(request, cart_id):
    template = loader.get_template('view_cart_details.html')
    user = request.user.username
    user_id = get_object_or_404(User, username=user)
    cart = get_object_or_404(Cart_id, cartID=cart_id)
    cartid = cart.id
    customer_name = cart.customer_name
    cart_items = CartItem.objects.filter(cart_ID=cartid)
    cart_id = cart_id
    context = {
        'cart_items': cart_items,
        'username': user,
        'customer_name': customer_name,
        'cart_id' : cart_id,
        'cart' : cart

    }
    if request.method == 'POST':
        part_number = request.POST['part_number']
        customer_name = customer_name
        item = CartItem.objects.filter(product_id=part_number, cart_ID=cartid)
        item.delete()
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse(template.render(context, request))


@login_required(login_url='login_user')
def Add_To_Cart(request, cart_id, part_number, quantity):
    cart = get_object_or_404(Cart_id, cartID=cart_id)
    customer_name = cart.customer_name
    part_number = part_number
    p = get_object_or_404(Stock, part_number=part_number)
    user = request.user.username
    user_id = get_object_or_404(User, username=user)
    product_in_cart = False
    cart_product = CartItem.objects.filter(product_id=part_number, cart_ID=cart )
    for cart_items in cart_product:
        if cart_items.product.part_number == p.part_number:
            cart_items.AugmentedQuantity(quantity)
            product_in_cart = True
    if not product_in_cart:
        user = request.user.username
        user_id = get_object_or_404(User, username=user)
        quantity = quantity
        ci = CartItem(product=p,userID=user_id,cart_ID=cart, quantity=quantity)
        ci.save()

    return redirect('create_cart', cart_id)



def checkout(request, cart_id):
    cartID = get_object_or_404(Cart_id, cartID=cart_id)
    cart = CartItem.objects.filter(cart_ID=cartID)
    total = sum(item.Total() for item in cart)
    total_words = convert_digit_to_word(total)
    template = loader.get_template('checkout.html')
    context = {
        'cart': cart,
        'total': total,
        'total_words': total_words,
        'cart_id': cart_id,
    }
    return HttpResponse(template.render(context, request))


def proceed_payment(request, cart_id):
    cartID = get_object_or_404(Cart_id, cartID=cart_id)
    cartID.is_checked_out = True
    cartID.save()
    return redirect('carts')


def Remove_All(request):
    item1 = CartItem.objects.all()
    item1.delete()
    item2 = Stock.objects.all()
    item2.delete()
    item3 = Cart_id.objects.all()
    item3.delete()

# Create your views here.
