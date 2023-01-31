from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product, MainCategory, Category, Subcategory, Brand


class TestBagViews(TestCase):
    """ Tests for Bag app views """

    def setUp(self):
        """
        Creates test objects (MainCategory, Category, Subcategory,
        Brand and Product)
        """

        self.main_category1 = MainCategory.objects.create(
            name='Makeup',
            slug='makeup',
        )

        self.category1 = Category.objects.create(
            main_category=self.main_category1,
            name='Face',
            friendly_name='Face',
            slug='face',
        )

        self.subcategory1 = Subcategory.objects.create(
            category=self.category1,
            name='foundation',
            friendly_name='Foundation',
            slug='foundation',
        )

        self.brand1 = Brand.objects.create(
            name='Makeup Brand',
            friendly_name='Makeup Brand',
            slug='makeup-brand',
            description='brand description goes here',
            is_featured=False,
        )

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

    # test get bag page view
    def test_get_bag_page(self):
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    # test add product to bag
    def test_can_add_product_to_bag(self):
        product = self.product1,

        response = self.client.post(
            f'/bag/add/{str(self.product1.id)}/',
            {'quantity': 2, 'redirect_url': 'view_bag'}
        )
        bag = self.client.session['bag']
        self.assertEqual(bag[str(self.product1.id)], 2)
        self.assertRedirects(response, '/bag/')

    # test update bag
    def test_can_update_bag(self):
        product = self.product1,

        # posts 5 quantities of product1
        response = self.client.post(
            f'/bag/add/{str(self.product1.id)}/',
            {'quantity': 5, 'redirect_url': 'view_bag'}
        )
        bag = self.client.session['bag']
        self.assertEqual(bag[str(self.product1.id)], 5)
        self.assertIn('bag', self.client.session)
        self.assertRedirects(response, '/bag/')

        # adjusts quantity of product1 from 5 to 3
        response = self.client.post(
            f'/bag/adjust/{str(self.product1.id)}/',
            {'quantity': 3, 'redirect_url': 'view_bag'}
        )
        bag = self.client.session['bag']
        self.assertEqual(bag[str(self.product1.id)], 3)
        self.assertIn('bag', self.client.session)

    # test remove product from bag
    def test_can_remove_product_from_bag(self):
        product = self.product1,

        self.client.post(
            f'/bag/add/{str(self.product1.id)}/',
            {'quantity': 2, 'redirect_url': 'view_bag'}
        )

        response = self.client.post(f'/bag/remove/{str(self.product1.id)}/')
