from django.test import TestCase
from products.models import Product, MainCategory, Category, Subcategory, Brand
from products.forms import ProductForm, BrandForm


class TestProductAndBrandForms(TestCase):
    """
        Tests for product forms and brand forms
        if fields are required
    """
    # start of tests for ProductForm
    def test_main_category_is_required_in_product_form(self):
        form = ProductForm({'main_category': ''})
        self.assertIn('main_category', form.errors.keys())
        self.assertEqual(form.errors['main_category'][0],
                         'This field is required.')

    def test_category_is_required_in_product_form(self):
        form = ProductForm({'category': ''})
        self.assertIn('category', form.errors.keys())
        self.assertEqual(form.errors['category'][0],
                         'This field is required.')

    def test_subcategory_is_required_in_product_form(self):
        form = ProductForm({'subcategory': ''})
        self.assertIn('subcategory', form.errors.keys())
        self.assertEqual(form.errors['subcategory'][0],
                         'This field is required.')

    def test_brand_is_required_in_product_form(self):
        form = ProductForm({'brand': ''})
        self.assertIn('brand', form.errors.keys())
        self.assertEqual(form.errors['brand'][0],
                         'This field is required.')

    def test_sku_is_required_in_product_form(self):
        form = ProductForm({'sku': ''})
        self.assertIn('sku', form.errors.keys())
        self.assertEqual(form.errors['sku'][0],
                         'This field is required.')

    def test_name_is_required_in_product_form(self):
        form = ProductForm({'name': ''})
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0],
                         'This field is required.')

    def test_slug_is_required_in_product_form(self):
        form = ProductForm({'slug': ''})
        self.assertIn('slug', form.errors.keys())
        self.assertEqual(form.errors['slug'][0],
                         'This field is required.')

    def test_description_is_required_in_product_form(self):
        form = ProductForm({'description': ''})
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0],
                         'This field is required.')

    def test_how_to_use_is_required_in_product_form(self):
        form = ProductForm({'how_to_use': ''})
        self.assertIn('how_to_use', form.errors.keys())
        self.assertEqual(form.errors['how_to_use'][0],
                         'This field is required.')

    def test_ingredients_is_required_in_product_form(self):
        form = ProductForm({'ingredients': ''})
        self.assertIn('ingredients', form.errors.keys())
        self.assertEqual(form.errors['ingredients'][0],
                         'This field is required.')

    def test_price_is_required_in_product_form(self):
        form = ProductForm({'price': ''})
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['price'][0],
                         'This field is required.')

    def test_image_is_required_in_product_form(self):
        form = ProductForm({'image': ''})
        self.assertIn('image', form.errors.keys())
        self.assertEqual(form.errors['image'][0],
                         'This field is required.')

    # def test_other_fields_are_not_required(self):
    #     form = ProductForm({
    #         'main_category': 'makeup',
    #         'category': 'face',
    #         'subcategory': 'foundation',
    #         'brand': 'makeup brand',
    #         'sku': 'axi-sk-fc-spt-0005',
    #         'name': 'new foundation',
    #         'slug': 'new-foundation',
    #         'is_featured': True,
    #         'description': 'product description goes here',
    #         'how_to_use': 'product how to use content goes here',
    #         'ingredients': 'product ingredients goes here',
    #         'price': 2.99,
    #         'has_sizes': False,
    #     })
    #     self.assertTrue(form.is_valid())

    # start of tests for BrandForm
    def test_brand_name_is_required_in_brand_form(self):
        form = BrandForm({'name': ''})
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0],
                         'This field is required.')

    def test_slug_is_required_in_brand_form(self):
        form = BrandForm({'slug': ''})
        self.assertIn('slug', form.errors.keys())
        self.assertEqual(form.errors['slug'][0],
                         'This field is required.')

    def test_description_is_required_in_brand_form(self):
        form = BrandForm({'description': ''})
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0],
                         'This field is required.')

    # def test_other_fields_are_not_required(self):
    #     form = BrandForm({
    #         'name': 'new brand',
    #         'slug': 'new-brand',
    #         'description': 'brand description goes here',
    #     })
    #     self.assertTrue(form.is_valid())
