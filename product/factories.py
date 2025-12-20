import factory
from django.contrib.auth.models import User
from product.models.category import Category
from product.models.product import Product
from order.models.order import Order


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker('email')
    username = factory.Faker('user_name')

    class Meta:
        model = User


class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("word")
    slug = factory.Faker("slug")
    description = factory.Faker("sentence")
    active = factory.Iterator([True, False])

    class Meta:
        model = Category   # ✅ apenas isso dentro da Meta


class ProductFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("word")
    price = factory.Faker("pydecimal", left_digits=4, right_digits=2, positive=True)
    active = True

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for category in extracted:
                self.categories.add(category)

    class Meta:
        model = Product   # ✅ import feito no topo


class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def products(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for product in extracted:
                self.products.add(product)

    class Meta:
        model = Order   # ✅ import feito no topo

