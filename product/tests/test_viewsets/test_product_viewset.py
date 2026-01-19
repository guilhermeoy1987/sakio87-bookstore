from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.urls import reverse

from order.factories import UserFactory
from product.factories import CategoryFactory, ProductFactory
from product.models import Product


class TestProductViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        # Usuário comum
        self.user = UserFactory()

        # Produto existente
        self.product = ProductFactory(
            title="pro controller",
            price=200.00,
        )

    # 🔓 PRODUTOS SÃO PÚBLICOS (GET)
    def test_get_all_products_without_authentication(self):
        response = self.client.get(
            reverse("product-list", kwargs={"version": "v1"})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        self.assertEqual(data["results"][0]["title"], self.product.title)

    # 🔐 NÃO AUTENTICADO NÃO CRIA PRODUTO
    def test_create_product_requires_authentication(self):
        category = CategoryFactory()

        data = {
            "title": "notebook",
            "price": 800.00,
            "categories_id": [category.id],
        }

        response = self.client.post(
            reverse("product-list", kwargs={"version": "v1"}),
            data=data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # 🔐 AUTENTICADO MAS NÃO ADMIN → PROIBIDO
    def test_create_product_authenticated_but_not_admin(self):
        token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        category = CategoryFactory()

        data = {
            "title": "notebook",
            "price": 800.00,
            "categories_id": [category.id],
        }

        response = self.client.post(
            reverse("product-list", kwargs={"version": "v1"}),
            data=data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # 🔐 ADMIN CRIA PRODUTO
    def test_create_product_admin(self):
        admin = UserFactory(is_staff=True, is_superuser=True)
        token = Token.objects.create(user=admin)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        category = CategoryFactory()

        data = {
            "title": "notebook",
            "price": 800.00,
            "categories_id": [category.id],
        }

        response = self.client.post(
            reverse("product-list", kwargs={"version": "v1"}),
            data=data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        product = Product.objects.get(title="notebook")
        self.assertEqual(product.price, 800.00)


