from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from products.models import Stock, Cart_id
from .models import PurchaseBook, Credit_ID, CreditRecord
from django.shortcuts import get_object_or_404
from products.cart import generate_credit_id


@login_required(login_url='login_user')
def documents(request):
    template = loader.get_template('document.html')
    return HttpResponse(template.render())


def view_purchasebook(request):
    pb = PurchaseBook.objects.all()
    template = loader.get_template('view_purchasebook.html')
    context = {
        'pb': pb,
    }
    return HttpResponse(template.render(context, request))

def purchaseBook(request):
    template = loader.get_template('purchasebook.html')
    stock = Stock.objects.all()
    user = request.user.username
    if request.method == 'POST':
        part_number = request.POST['part_number']
        quantity_in = request.POST['quantity']
        location = request.POST['location']
        item = get_object_or_404(Stock, part_number=part_number)
        pb = PurchaseBook(part_number=item, quantity_in=quantity_in, location=location)
        pb.save()
        balance = item.balance
        item.balance = int(balance) + int(quantity_in)
        item.save()
        context = {
            'stock': stock,
            'username': user,
        }
        return HttpResponse(template.render(context, request))
    else:
        context = {
            'stock': stock,
            'username': user,
        }
        return HttpResponse(template.render(context, request))


def newProduct(request):
    template = loader.get_template('newproduct.html')
    user = request.user.username
    product_in_stock = False
    context = {
        'username': user,
    }
    if request.method == 'POST':
        part_name = request.POST['part_name']
        part_number = request.POST['part_number']
        location = request.POST['location']
        quantity = request.POST['quantity']
        price = request.POST['price']
        stock_item = Stock.objects.all()

        for x in stock_item:
            if x.part_number == part_number:
                item = get_object_or_404(Stock, part_number=part_number)
                pb = PurchaseBook(part_number=item, location=location, quantity_in=quantity, price=price)
                pb.save()
                balance = item.balance
                item.balance = int(balance) + int(quantity)
                item.save()
                product_in_stock = True
        if not product_in_stock:
            stock = Stock(name=part_name, part_number=part_number, location=location, balance=quantity, price=price)
            stock.save()
            pb = PurchaseBook(part_number=stock, location=location, quantity_in=quantity, price=price)
            pb.save()
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse(template.render(context, request))


def credit_record(request):
    if request.method == 'POST':
        credit_id = generate_credit_id()
        customer_name = request.POST['customer_name']
        new = Credit_ID(customer_name=customer_name, customer_id=credit_id)
        new.save()
        return redirect('credit_record')
    else:
        credit_id = Credit_ID.objects.all()
        template = loader.get_template('credit.html')
        context = {
            'credit_id': credit_id,
        }
        return HttpResponse(template.render(context, request))


def credit_details(request, credit_id):
    credit = get_object_or_404(Credit_ID, customer_id=credit_id)
    record = CreditRecord.objects.filter(customer=credit)
    template = loader.get_template('credit_detail.html')
    context = {
        'record': record
    }
    return HttpResponse(template.render(context, request))


# Create your views here.

# Create your views here.
