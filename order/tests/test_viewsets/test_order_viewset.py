from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from product.factories import CategoryFactory, ProductFactory
from order.factories import UserFactory, OrderFactory


class TestOrderViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        # Usuário autenticado
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)

        # Dados base
        self.category = CategoryFactory(title="technology")

        self.product = ProductFactory(
            title="mouse",
            price=100,
            categories=[self.category],
        )

        self.order = OrderFactory(
            products=[self.product],
            user=self.user,
        )

    def test_order_list(self):
        url = reverse("order-list", kwargs={"version": "v1"})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        # Paginação do DRF
        self.assertIn("results", data)
        self.assertEqual(data["count"], 1)

        order_data = data["results"][0]

        product_data = order_data["products"][0]

        self.assertEqual(
            product_data["title"],
            self.product.title,
        )
        self.assertEqual(
            product_data["price"],
            self.product.price,
        )
        self.assertEqual(
            product_data["active"],
            self.product.active,
        )

        category_data = product_data["categories"][0]
        self.assertEqual(
            category_data["title"],
            self.category.title,
        )

    def test_create_order(self):
        product = ProductFactory(categories=[self.category])

        data = {
            "products_id": [product.id],
            "user": self.user.id,
        }

        url = reverse("order-list", kwargs={"version": "v1"})
        response = self.client.post(
            url,
            data=data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
