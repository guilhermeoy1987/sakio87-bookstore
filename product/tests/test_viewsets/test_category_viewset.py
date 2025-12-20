import json
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from product.factories import CategoryFactory
from product.models import Category


class CategoryViewSetTest(APITestCase):
    client = APIClient()

    def setUp(self):
        # Cria uma categoria de teste
        self.category = CategoryFactory(title="books")
        self.base_url = reverse("category-list", kwargs={"version": "v1"})

    def test_get_all_category(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        category_data = response.json()
        self.assertEqual(category_data["results"][0]["title"], self.category.title)

    def test_create_category(self):
        data = {"title": "technology"}
        response = self.client.post(self.base_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_category = Category.objects.get(title="technology")
        self.assertEqual(created_category.title, "technology")

    def test_delete_category(self):
        # cria uma categoria para deletar
        category_to_delete = CategoryFactory(title="delete-me")
        delete_url = reverse("category-detail", kwargs={"version": "v1", "pk": category_to_delete.id})
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Category.objects.filter(id=category_to_delete.id).exists())

    def test_get_single_category(self):
        url = reverse("category-detail", kwargs={"version": "v1", "pk": self.category.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data["title"], self.category.title)

