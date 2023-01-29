from django.test import TestCase, Client
import uuid
from django.urls import reverse
from profiles.models import User
from .models import Order, OrderLineItem
from products.models import Product, MainCategory, Category, Subcategory, Brand


class TestOrderModels(TestCase):
    """ Draft testing checkout"""

    def setUp(self):
        # create a test user object
        self.user1 = User.objects.create(
            email='test@test.com',
            username='testuser',
            password='password',
        )
        # logged_in = self.client.login(email=self.user1.email,
        #                               password=self.user1.password)
        # self.assertTrue(logged_in)

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

        # self.order1 = Order.objects.create(
        #     user_profile=self.user_profile1,
        #     full_name='Test User',
        #     email='test@test.com',
        #     phone_number='12345678',
        #     street_address1='My Street1',
        #     street_address2='My Street2',
        #     town_or_city='London',
        #     county='Anywhere',
        #     postcode='12345',
        #     country='GB',
        # )
        # self.order1.save()
        # self.get_order_number = Order.objects.get(id=1).order_number
        # self.orderlineitem1 = OrderLineItem.objects.create(
        #     order=self.order1,
        #     product=self.product1,
        #     quantity=1,
        # )
        # print(orderlineitem1)

        # def test_save_order(self):
        #     """ test order is saved """
        #     self.assertEqual(self.order1.order_number, self.get_order_number)

        # def test_order_str(self):
        #     """ test order str """
        #     self.assertEqual(str(self.order1), self.get_order_number)

        # def test_get_orderlineitems(self):
        #     """ test order items """
        #     self.assertEqual(self.order1.get_orderlineitems()[0],
        #                      self.orderline)

    def test_checkout_page(self):
        """ test checkout page if user is authenticated """

        # set bag session
        session = self.client.session
        session['bag'] = {str(self.product1.id): 1}
        session.save()

        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')
