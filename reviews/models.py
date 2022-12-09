from django.db import models
from products.models import Product, Category
from django.contrib.auth.models import User


class Review(models.Model):
    """ Review model """
    product = models.ForeignKey(Product, null=True, blank=True,
                                on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    friendly_name = models.CharField(max_length=30, null=True, blank=True)
    content = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True, blank=False, null=False)
    is_featured = models.BooleanField(default=False)

    class Meta:
        """ Meta class for Review model """
        ordering = ['-date']

    def __str__(self):
        """ String representation of Brand model """
        return self.title

    def get_friendly_name(self):
        return self.friendly_name
