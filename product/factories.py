import factory
from django.contrib.auth.models import User

from product.models.category import Category
from product.models.product import Product


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = factory.Faker("email")


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    title = factory.Faker("word")
    slug = factory.Faker("slug")
    description = factory.Faker("sentence")
    active = factory.Iterator([True, False])


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    title = factory.Sequence(lambda n: f"product-{n}")
    price = 100
    active = True

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        """
        Permite:
        ProductFactory(categories=[cat1, cat2])
        """
        if not create:
            return

        if extracted:
            for category in extracted:
                self.categories.add(category)
