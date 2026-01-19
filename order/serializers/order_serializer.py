from rest_framework import serializers
from order.models import Order
from product.models import Product
from product.serializers.product_serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True, many=True)
    products_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        write_only=True,
        many=True
    )
    total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ["products", "products_id", "total"]
        read_only_fields = ("products", "total")

    def get_total(self, instance):
        return sum(product.price for product in instance.products.all())

    def create(self, validated_data):
        products = validated_data.pop("products_id")
        order = Order.objects.create(**validated_data)
        order.products.set(products)
        return order
