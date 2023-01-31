from django.test import TestCase
from django.contrib.auth.models import User
from wishlist.models import Wishlist


class TestWishlistViews(TestCase):
    """ Test for wishlist app views """

    def setUp(self):
        """
        Creates test user
        """
        testuser = User.objects.create_user(
            username='test_username',
            password='secret',
            email='testuser@email.com'
        )
        testuser.save()

    def test_can_get_wishlist_page(self):
        """ test to get wishlist page """
        logged_in = self.client.login(username='test_username',
                                      password='secret')
        self.assertTrue(logged_in)
        testuser = User.objects.get(username='test_username')
        response = self.client.get(f'/wishlist/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wishlist/wishlist.html')
