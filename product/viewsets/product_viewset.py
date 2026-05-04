from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny # Troque IsAuthenticated por IsAdminUser

from product.models import Product
from product.serializers.product_serializer import ProductSerializer

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_permissions(self):
        # Se for criar, editar ou deletar, exige ser ADMIN (is_staff=True)
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        
        # Para listar ou ver detalhes, qualquer um (mesmo deslogado) pode
        return [AllowAny()]

    def get_queryset(self):
        return Product.objects.all().order_by("id")

