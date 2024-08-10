from django.test import TestCase
from django.contrib.auth import get_user_model


# Create your tests here.
class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='bob', email='bob@email.com', password='bobthebest123'
        )
        self.assertEqual(user.username, 'bob')
        self.assertEqual(user.email, 'bob@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superbob', email='superbob@email.com', password='superbobthebest123'
        )
        self.assertEqual(admin_user.username, 'superbob')
        self.assertEqual(admin_user.email, 'superbob@email.com')
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_active)
