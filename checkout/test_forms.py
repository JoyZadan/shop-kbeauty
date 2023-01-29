from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):
    """ Tests for Checkout app forms if fields are required """

    def test_full_name_is_required_in_orderform(self):
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(form.errors['full_name'][0],
                         'This field is required.')

    def test_email_is_required_in_orderform(self):
        form = OrderForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0],
                         'This field is required.')

    def test_phone_number_is_required_in_orderform(self):
        form = OrderForm({'phone_number': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(form.errors['phone_number'][0],
                         'This field is required.')

    def test_street_address1_is_required_in_orderform(self):
        form = OrderForm({'street_address1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(form.errors['street_address1'][0],
                         'This field is required.')

    def test_town_or_city_is_required_in_orderform(self):
        form = OrderForm({'town_or_city': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(form.errors['town_or_city'][0],
                         'This field is required.')

    def test_country_is_required_in_orderform(self):
        form = OrderForm({'country': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(form.errors['country'][0],
                         'This field is required.')

    def test_street_address2_is_not_required_in_orderform(self):
        form = OrderForm({
            'full_name': 'My Name',
            'email': 'test@test.com',
            'phone_number': '12345678',
            'street_address1': 'My Street',
            'town_or_city': 'My Town',
            'country': 'GB',
            })
        self.assertTrue(form.is_valid())
