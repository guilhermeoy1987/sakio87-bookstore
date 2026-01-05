from rest_framework import viewsets
from .models import Order
# order/viewsets.py
from .serializers.order_serializer import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
