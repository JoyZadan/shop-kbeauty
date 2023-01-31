from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product, MainCategory, Category, Subcategory, Brand
from reviews.models import Review


class TestReviewsViews(TestCase):
    """ Test for reviews app views """

    def setUp(self):
        """
        Creates test user, review and product objects (MainCategory, Category,
        Subcategory, Brand and Product)
        """

        testsuperuser = User.objects.create_superuser(
            username='testsuperuser_username',
            password='supersecret',
            email='testsuperuseuser@email.com'
        )
        testsuperuser.save()

        testuser = User.objects.create_user(
            username='test_username',
            password='secret',
            email='testuser@email.com'
        )
        testuser.save()

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
            image='image-file',
        )

        self.review1 = Review.objects.create(
            product=self.product1,
            user=testuser,
            title='test review',
            content='test review content goes here',
        )

    def test_can_get_reviews_page(self):
        """ test to get reviews page """
        response = self.client.get(f'/reviews/reviews/{str(self.product1.id)}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/reviews.html')

    def test_can_get_add_review(self):
        """ test to get add review page """
        logged_in = self.client.login(username='test_username',
                                      password='secret')
        self.assertTrue(logged_in)
        testuser = User.objects.get(username='test_username')
        response = self.client.get(f'/reviews/add_review/\n'
                                   f'{str(self.product1.id)}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/add_review.html')

    def test_can_get_edit_review(self):
        """ test to get edit review page, if logged in user is superadmin """
        logged_in = self.client.login(username='testsuperuser_username',
                                      password='supersecret')
        self.assertTrue(logged_in)
        testsuperuser = User.objects.get(username='testsuperuser_username')
        response = self.client.get(f'/reviews/edit_review/\n'
                                   f'{str(self.review1.id)}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/edit_review.html')
