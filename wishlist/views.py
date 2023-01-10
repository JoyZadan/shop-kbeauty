from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from profiles.models import UserProfile
from products.models import Product
from wishlist.models import Wishlist


@login_required
def wishlist(request):
    """ A view to show the user's wishlist """
    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = Wishlist.objects.filter(user_profile=user)

    template = 'wishlist/wishlist.html'

    context = {
        'wishlist': wishlist
    }

    return render(request, template, context)


def add_to_wishlist(request, product_id):
    """ A view to add product to a logged in user's wishlist """
    if not request.user.is_authenticated:
        messages.error(request,
                       'Sorry, you need to be logged in to add your wishlist.')
        return redirect(reverse('account_login'))

    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    wishlist = Wishlist.objects.create(user_profile=user, product=product)
    messages.info(request, 'Product added to your wishlist!')

    return redirect(reverse('product_detail', args=[product.id]))
