from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework.test import APIClient, APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status

from product.factories import CategoryFactory
from product.models import Category


class CategoryViewSetTest(APITestCase):
    client = APIClient()

    def setUp(self):
        self.category = CategoryFactory(title="books")
        self.base_url = reverse("category-list", kwargs={"version": "v1"})

        # Admin
        self.admin = User.objects.create_superuser(
            username="admin",
            password="123456",
            email="admin@test.com"
        )
        token = Token.objects.create(user=self.admin)
        self.admin_token = token.key

    # 🔓 GET público
    def test_get_all_category(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        self.assertEqual(data["results"][0]["title"], self.category.title)

    # 🔓 GET público (detail)
    def test_get_single_category(self):
        url = reverse(
            "category-detail",
            kwargs={"version": "v1", "pk": self.category.id}
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["title"], self.category.title)

    # ❌ POST sem autenticação
    def test_create_category_without_authentication(self):
        data = {"title": "technology"}

        response = self.client.post(self.base_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ✅ POST como admin
    def test_create_category_as_admin(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.admin_token
        )

        data = {"title": "technology"}

        response = self.client.post(self.base_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(Category.objects.filter(title="technology").exists())

    # ❌ DELETE sem autenticação
    def test_delete_category_without_authentication(self):
        category_to_delete = CategoryFactory()

        url = reverse(
            "category-detail",
            kwargs={"version": "v1", "pk": category_to_delete.id}
        )

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ✅ DELETE como admin
    def test_delete_category_as_admin(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.admin_token
        )

        category_to_delete = CategoryFactory()

        url = reverse(
            "category-detail",
            kwargs={"version": "v1", "pk": category_to_delete.id}
        )

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(
            Category.objects.filter(id=category_to_delete.id).exists()
        )
