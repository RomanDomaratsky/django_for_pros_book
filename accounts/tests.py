from django.test import TestCase
from django.urls import reverse, resolve
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


class SignUpPageTests(TestCase):
    username = "newuser"
    email = "newuser@email.com"

    def setUp(self):
        url = reverse("account_signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "account/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "I should bot be on this page")

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, "newuser")
        self.assertEqual(get_user_model().objects.all()[0].email, "newuser@email.com")
