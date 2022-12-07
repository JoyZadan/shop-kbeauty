from django.test import TestCase


class TestViews(TestCase):
    """ Test correct rendering for home url """
    def test_get_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
