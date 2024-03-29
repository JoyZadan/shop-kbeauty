from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from products.models import Product, MainCategory, Category, Subcategory, Brand


class TestViews(TestCase):
    """ Test for products app views """

    def setUp(self):
        """
        Creates test user and product objects (MainCategory, Category,
        Subcategory, Brand and Product)
        """

        testsuperuser = User.objects.create_superuser(
            username='testsuperuser_username',
            password='secret',
            email='testsuperuseuser@email.com'
        )
        testsuperuser.save()

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

    def test_can_get_products_page(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_can_get_messages_from_search_with_no_search_term(self):
        """ test get error message when no search term was used from search """
        response = self.client.get('/products/', {'q': ''})
        self.assertRedirects(response, '/products/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         "You didn't enter any search criteria!")

    def test_can_get_all_products_from_search(self):
        """ test to get all products page from search """
        response = self.client.get('/products/', {'search_term': 'foundation',
                                   'current_subcategories': 'foundation'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_sort(self):
        """ test product sorting with parameters """
        response = self.client.get('/products/', {'sort': 'discount',
                                   'direction': 'desc'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_add_product_page(self):
        """ create test login for superuser and get add product page """
        logged_in = self.client.login(username='testsuperuser_username',
                                      password='secret')
        self.assertTrue(logged_in)
        testsuperuser = User.objects.get(username='testsuperuser_username')
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')
