from django.test import TestCase
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from checkout.models import Order
from profiles.models import UserProfile


class TestProfilesViews(TestCase):
    """ Tests for profiles app views """

    def setUp(self):
        testuser = User.objects.create_user(
            username='test_username',
            password='secret',
            email='testuser@email.com'
        )
        testuser.save()

        Order.objects.create(
            order_number='1234567890',
            user_profile=UserProfile.objects.get(user=testuser),
            full_name='Test User',
            email='testuser@email.com',
            phone_number='12345678',
            country='GB',
            postcode='12345',
            town_or_city='London',
            street_address1='My Street',
            county='Anywhere',
        )

    def tearDown(self):
        """
        Test delete test user and order
        """
        User.objects.all().delete()
        Order.objects.all().delete()

    def test_get_profile_page(self):
        """
        Tests that a test user can log in, access their profile page
        (get) and verifies
        """
        self.client.login(username='test_username', password='secret')
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_post_profile_page(self):
        """
        Tests that a test user can log in, access their profile page
        (post) and verifies
        """
        self.client.login(username='test_username', password='secret')
        response = self.client.post('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_get_order_detail_page(self):
        """
        Tests that a test user can log in, access their test order
        order history and verifies
        """
        self.client.login(username='test_username', password='secret')
        testuser = User.objects.get(username='test_username')
        order = Order.objects.get(email=testuser.email)
        response = self.client.get('/profile/order_history/' +
                                   order.order_number)
        self.assertEqual(response.status_code, 200)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'This is a past confirmation for '
                         'order number 1234567890. ' +
                         'A confirmation email was sent on the order date.')
