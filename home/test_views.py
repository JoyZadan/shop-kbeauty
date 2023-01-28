from django.test import TestCase


class TestHomeViews(TestCase):
    """ Test correct rendering for home url """

    def test_get_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_get_skincare_tips_page(self):
        response = self.client.get('/skincare_tips/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/skincare_tips.html')

    def test_get_privacy_policy_page(self):
        response = self.client.get('/privacy_policy/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/privacy_policy.html')

    def test_get_terms_and_conditions_page(self):
        response = self.client.get('/terms_and_conditions/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/terms_and_conditions.html')

    def test_get_return_and_refund_page(self):
        response = self.client.get('/return_and_refund_policy/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/return_and_refund_policy.html')

    def test_get_shipping_policy_page(self):
        response = self.client.get('/shipping_policy/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/shipping_policy.html')
