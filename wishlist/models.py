from django.db import models
from profiles.models import UserProfile
from products.models import Product


class Wishlist(models.Model):
    """ Wishlist model """
    user_profile = models.ForeignKey(UserProfile, null=True, blank=True,
                                     on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, blank=True,
                                on_delete=models.CASCADE)
    added = models.DateField(auto_now_add=True, blank=False, null=False)

    def __str__(self):
        """ String representation of Wishlist model """
        return self.name
