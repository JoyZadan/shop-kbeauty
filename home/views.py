from django.shortcuts import render
from products.models import Product, Brand


def index(request):
    """ A view to return the index page including the featured brands """
    brands = Brand.objects.all()
    products = Product.objects.all()
    context = {
        'brands': brands,
        'products': products,
    }
    return render(request, 'home/index.html', context)
