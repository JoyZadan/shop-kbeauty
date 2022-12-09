from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.messages import get_messages
from django.utils.text import slugify

from django.contrib.auth.models import User
from .models import Review
from products.models import Product, Category, Subcategory, MainCategory


class TestProductViews(TestCase):
    """
    Test product views
    """
    def setUp(self):
        """
        Create mock review
        """
        self.admin = User.objects.create(
            username='admin',
            password='test1ing123',
        )

        self.client.force_login(self.admin)

        self.main_category = MainCategory.objects.create(
            name='test',
        )

        self.category = Category.objects.create(
            name='test',
            friendly_name='Test 1',
            main_category='test',
        )

        self.subcategory = Subcategory.objects.create(
            name='test',
            friendly_name='Test 1',
            category='test',
            main_category='test',
        )

        self.brand = Brand.objects.create(
            name='test',
            friendly_name='Test 1',
            description='so hard',
            image_url='media.png',
            is_featured=True,
        )

        self.product = Product.objects.update_or_create(
            main_category=self.main_category,
            category=self.category.main_category,
            subcategory=self.subcategory.category.main_category,
            brand=self.brand,
            name='product1',
            sku='sk-728',
            availability='1',
            description='testing 12345',
            how_to_use='testing use',
            ingredients='testing ingredients',
            condition='mint',
            has_sizes=False,
            price=2.00,
            image_url='media.png',
        )

        self.review = Review.objects.create(
            product=self.product,
            user=self.admin,
            content='testing 12345',
            title='test',
            is_featured=False,
            friendly_name='test',
        )

    def test_reviews_page(self):
        """
        Test reviews url
        """
        response = self.client.get(f'/reviews/reviews/\n'
                                   f'{self.product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/reviews.html')
