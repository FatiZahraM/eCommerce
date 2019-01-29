from django.shortcuts import render
from .models import Product, ProductImage


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    template = 'products/home.html'
    return render(request, template, context)


def all(request):
    products = Product.objects.all()
    context = {'products': products}
    template = 'products/all.html'
    return render(request, template, context)


def single(request, slug):
    product = Product.objects.get(slug=slug)
    images = ProductImage.objects.filter(product=product)
    context = {'product': product, 'images': images}
    template = 'products/single.html'
    return render(request, template, context)


def search(request):
    if request.method == 'GET':   # this will be GET now
        product_name = request.GET.get('search')   # do some research what it does
        status = Product.objects.filter(title=product_name)    # filter returns a list so you might consider skip except part

        return render(request, 'results.html', {'products': status})

    else:
                return render(request, 'results.html', {})



