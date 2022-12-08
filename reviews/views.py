from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from products.models import Product
from .models import Review
from .forms import ReviewForm
from profiles.models import UserProfile


def reviews(request, product_id):
    """ A view to show review form """
    product = get_object_or_404(Product, pk=product_id)

    reviews = Review.objects.filter(product=product)
    template = 'reviews/reviews.html'

    context = {
        'reviews': reviews,
    }

    return render(request, template, context)


def add_review(request, product_id):
    """ Renders a form to allow user to add a review """
    user = UserProfile.objects.get(user=request.user)
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, "New product review added.")
            return redirect(reverse('review_detail', args=[review.id]))
        else:
            messages.error(request, "Form invalid, please try again.")
            return redirect(reversed('product_details', args=[product.id]))
    else:
        form = ReviewForm()

    template = 'reviews/add_review.html'

    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
