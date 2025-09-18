
import factory
from django.contrib.auth.models import User
from product.models import Product, Category
from order.models import Order
from product.factories import ProductFactory


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker('pystr')
    username = factory.Faker('pystr')

    class Meta:
        model = User


class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("pystr")
    slug = factory.Faker("pystr")
    description = factory.Faker("pystr")
    active = factory.Iterator([True, False])

    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("pystr")
    price = factory.Faker("pyint")
    category = factory.SubFactory(CategoryFactory)  # ForeignKey

    class Meta:
        model = Product


class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def product(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for product in extracted:
                self.product.add(product)

    class Meta:
        model = Order
