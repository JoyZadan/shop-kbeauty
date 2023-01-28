from django.test import TestCase
from .forms import OrderForm


class TestCheckoutViews(TestCase):
    """ Test correct rendering for checkout url """

    def test_get_checkout_page_if_bag_is_empty(self):
        response = self.client.get('/checkout/')
        self.assertTrue(response, '/products')
