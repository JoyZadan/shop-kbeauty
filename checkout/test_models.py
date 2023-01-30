from django.test import TestCase
from .models import Order
from products.models import Product, MainCategory, Category, Subcategory, Brand


class TestOrderModels(TestCase):
    """ Tests for the checkout models """

    def setUp(self):

        # create test main_category object
        self.main_category1 = MainCategory.objects.create(
            name='Makeup',
            slug='makeup',
        )

        # create test category object
        self.category1 = Category.objects.create(
            main_category=self.main_category1,
            name='Face',
            friendly_name='Face',
            slug='face',
        )

        # create test subcategory object
        self.subcategory1 = Subcategory.objects.create(
            category=self.category1,
            name='foundation',
            friendly_name='Foundation',
            slug='foundation',
        )

        # create test brand object
        self.brand1 = Brand.objects.create(
            name='Makeup Brand',
            friendly_name='Makeup Brand',
            slug='makeup-brand',
            description='brand description goes here',
            is_featured='False',
        )

        # create test product object
        self.product1 = Product.objects.create(
            main_category=self.main_category1,
            category=self.category1,
            subcategory=self.subcategory1,
            brand=self.brand1,
            sku='axi-sk-fc-spt-0005',
            name='New Foundation',
            slug='new-foundation',
            is_featured=True,
            total_quantity=100,
            availability=100,
            description='new foundation description goes here',
            how_to_use='new foundation how to use goes here',
            ingredients='new foundation ingredients goes here',
            has_sizes=False,
            price=26.99,
            discount=0.00,
            original_price=26.99,
            image_url='image_url',
        )

        # create test order object
        self.order1 = Order.objects.create(
            order_number='1234567890',
            full_name='Test User',
            email='testuser@email.com',
            phone_number='12345678',
            country='GB',
            postcode='12345',
            town_or_city='London',
            street_address1='My Street',
            county='Anywhere',
        )

    def test_order_str_method(self):
        """ Test the order number string """
        self.order1 = Order.objects.get(email='testuser@email.com')
        self.assertEqual(str(self.order1), self.order1.order_number)

    def test_checkout_page(self):
        """ test checkout page if user is authenticated """

        # set bag session
        session = self.client.session
        session['bag'] = {str(self.product1.id): 1}
        session.save()

        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')
