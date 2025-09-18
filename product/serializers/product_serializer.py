from rest_framework import serializers
from product.models.product import Product
from product.models.category import Category
from product.serializers.category_serializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    # Leitura: mostra categorias aninhadas
    categories = CategorySerializer(read_only=True, many=True)

    # Escrita: aceita lista de IDs de categorias
    categories_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True,
        many=True
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "price",
            "active",
            "categories",     # leitura (detalhada)
            "categories_id",  # escrita (via IDs)
        ]

    def create(self, validated_data):
        categories_data = validated_data.pop("categories_id")
        product = Product.objects.create(**validated_data)
        product.categories.set(categories_data)  # associa categorias
        return product

    def update(self, instance, validated_data):
        categories_data = validated_data.pop("categories_id", None)

        # Atualiza campos simples
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if categories_data is not None:
            instance.categories.set(categories_data)

        instance.save()
        return instance


