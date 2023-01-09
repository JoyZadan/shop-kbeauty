from django.shortcuts import render, get_object_or_404
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
