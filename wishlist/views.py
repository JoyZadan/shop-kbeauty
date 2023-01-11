from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import Http404
from django.conf import settings
from django.contrib import messages

from profiles.models import UserProfile
from products.models import Product
from wishlist.models import Wishlist


def wishlist(request):
    """ A view to show the user's wishlist """
    if not request.user.is_authenticated:
        messages.error(request,
                       'Sorry, you need to be logged in to add your Wishlist.')
        return redirect(reverse('account_login'))

    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = Wishlist.objects.filter(user_profile=user)

    template = 'wishlist/wishlist.html'

    context = {
        'wishlist': wishlist,
    }

    return render(request, template, context)


def add_to_wishlist(request, product_id):
    """
        A view to add product to a logged in user's wishlist
        and prevents users from adding products that are
        already in their wishlist
    """
    if not request.user.is_authenticated:
        messages.error(request,
                       'Sorry, you need to be logged in to add your Wishlist.')
        return redirect(reverse('account_login'))

    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    # checks if a product is already in a user's wishlist
    existing = Wishlist.objects.filter(product=product,
                                       user_profile=user).exists()
    if existing:
        messages.error(request, 'This product is already in your Wishlist!')
        return redirect(reverse('product_detail', args=[product.id]))
    else:
        wishlist_item = Wishlist.objects.create(user_profile=user,
                                                product=product)
    messages.info(request,
                  f'{product.name} has been added to your Wishlist!')

    return redirect(reverse('product_detail', args=[product.id]))


def remove_from_wishlist(request, product_id):
    """ A view to remove products from wishlist """
    if not request.user.is_authenticated:
        messages.error(request,
                       'Sorry, you need to be logged in to add your Wishlist.')
        return redirect(reverse('account_login'))

    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    Wishlist.objects.filter(product=product,
                            user_profile=user).delete()
    messages.info(request,
                  f'{product.name} has been removed from your Wishlist!')

    return redirect(reverse('product_detail', args=[product.id]))
