from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Cart
from products.models import Product

# Create your views here.


def view(request):
    carts = Cart.objects.all()[0]
    context = {'carts': carts}
    template = 'carts/view.html'
    return  render(request, template, context)


def update_cart(request, slug):
    carts = Cart.objects.all()[0]
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    except:
        pass
    if not product in carts.products.all():
            carts.products.add(product)
    else:
        carts.products.remove(product)

    new_total = 0.00
    for item in carts.products.all():
        new_total += float(item.price)
    carts.total = new_total
    carts.save()

    return redirect ('carts')