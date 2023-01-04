from django.shortcuts import render
from products.models import Product, Brand
from django.http import JsonResponse


def index(request):
    """ A view to return the index page including the featured brands """
    brands = Brand.objects.all()
    products = Product.objects.all()
    context = {
        'brands': brands,
        'products': products,
    }
    return render(request, 'home/index.html', context)


def skincare_tips(request):
    """ A view to render the k-beauty tips page """

    return render(request, 'home/skincare_tips.html')


def privacy_policy(request):
    """ A view to render the privacy policy page """

    return render(request, 'home/privacy_policy.html')


def terms_and_conditions(request):
    """ A view to render the terms and conditions page """

    return render(request, 'home/terms_and_conditions.html')


def return_and_refund_policy(request):
    """ A view to render the return and refund policy page """

    return render(request, 'home/return_and_refund_policy.html')


def shipping_policy(request):
    """ A view to render the shipping policy page """

    return render(request, 'home/shipping_policy.html')
