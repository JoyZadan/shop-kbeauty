from django.test import TestCase


class TestViews(TestCase):
    """ Test correct rendering for bag url """
    def test_bag_page(self):
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')
