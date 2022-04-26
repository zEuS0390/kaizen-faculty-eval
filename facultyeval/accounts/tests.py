from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
class AccountsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.login = reverse("accounts:login")
        self.register = reverse("accounts:register")

    def test_login_GET(self):
        response = self.client.get(self.login)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/login.html")

    def test_register_GET(self):
        response = self.client.get(self.register)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/register.html")

    def test_login_POST(self):
        user = User.objects.create(username='testuser')
        user.is_superuser = True
        user.is_active = True
        user.set_password('12345')
        user.save()
        self.client.login(username="testuser", password="12345")
        user = User.objects.filter(username="testuser").first()
        response = self.client.post(self.login, {
            "username": user.username,
            "password": user.password
        })
        self.assertEquals(response.status_code, 302)
        