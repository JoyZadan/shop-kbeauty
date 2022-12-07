from django.test import TestCase


class TestViews(TestCase):
    """ Test all_products view for rendering correct template """
    def test_products_page(self):  # passed test products.test_views
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
