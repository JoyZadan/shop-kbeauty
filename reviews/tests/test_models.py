from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product, MainCategory, Category, Subcategory, Brand
from reviews.models import Review


class TestReviewsModels(TestCase):
    """ Test for reviews app models """

    def setUp(self):
        """
        Creates test product objects (MainCategory, Category, Subcategory,
        Brand and Product)
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
            is_featured=True,
        )

    def test_review_str_method(self):
        """ tests the string representation of the review model """
        review = Review(title='test review')
        self.assertEqual(str(review), review.title)

    def test_review_is_featured(self):
        """ test the review is featured """
        self.assertEqual(self.review1.is_featured, True)
