from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from products.models import Product
from .models import Review
from .forms import ReviewForm


def reviews(request, product_id):
    """ A view to show review form """
    product = get_object_or_404(Product, pk=product_id)

    reviews = Review.objects.filter(product=product)
    template = 'reviews/reviews.html'

    context = {
        'reviews': reviews,
    }

    return render(request, template, context)
