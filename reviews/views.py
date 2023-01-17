from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Review
from .forms import ReviewForm
from profiles.models import UserProfile


def reviews(request, product_id):
    """ A view to show all available reviews for current product """
    product = get_object_or_404(Product, pk=product_id)

    reviews = Review.objects.filter(product=product)
    template = 'reviews/reviews.html'

    context = {
        'reviews': reviews,
        'product': product,
    }

    return render(request, template, context)


def add_review(request, product_id):
    """ Renders a form to allow users to add a review """
    if not request.user.is_authenticated:
        messages.error(request,
                       'Sorry, you need to be logged in to add a review.')
        return redirect(reverse('account_login'))

    user = UserProfile.objects.get(user=request.user)
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        review_form = ReviewForm(request.POST)

        if review_form.is_valid():
            review = review_form.save()
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, "New product review added.")
            return redirect(reverse('review_detail', args=[review.id]))
        else:
            messages.error(request, "Form invalid, please try again.")
            return redirect(reverse('product_detail', args=[product.id]))
    else:
        review_form = ReviewForm()

    template = 'reviews/add_review.html'

    context = {
        'review_form': review_form,
        'product': product,
    }

    return render(request, template, context)


def review_detail(request, review_id):
    """
        A view to display details individual reviews
    """
    review = get_object_or_404(Review, pk=review_id)

    template = 'reviews/review_detail.html'

    context = {
        'review': review,
    }

    return render(request, template, context)


@login_required()
def edit_review(request, review_id):
    """ Views to enable superusers to edit a review """
    if not request.user.is_authenticated:
        messages.error(request,
                       'Sorry, you need to be logged in to add a review.')
        return redirect(reverse('account_login'))

    review = get_object_or_404(Review, pk=review_id)
    product = Product.objects.filter(review=review)

    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES, instance=review)
        if review_form.is_valid():
            review_form.save()
            messages.success(request, f'Successfully updated review.')
            return redirect(reverse('review_detail', args=[review.id]))
        else:
            print("Form invalid")
            messages.error(request, f'Failed to update review.')
    else:
        review_form = ReviewForm(instance=review)
        messages.info(request, f'You are editing {review.title}')

    template = 'reviews/edit_review.html'

    context = {
        'review': review,
        'product': product,
        'review_form': review_form,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """
    Delete specific review
    """

    review = get_object_or_404(Review, pk=review_id)

    review.delete()

    messages.success(request, "Review successfully deleted")
    return redirect(reverse('products'))
