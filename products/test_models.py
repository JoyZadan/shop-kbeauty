from django.test import TestCase
from django.template.defaultfilters import slugify
from products.models import Product


class ModelsTestCase(TestCase):
    def test_product_has_slug(self):
        """Products are given slugs correctly when saving"""
        # not NULL constraints being caused by previous migrations!
        product = Product.objects.create(name="My first product")

        product.save()
        self.assertEqual(product.slug, slugify(product.name))
