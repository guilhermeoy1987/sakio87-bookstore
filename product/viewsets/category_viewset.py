from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser

from product.models import Category
from product.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    """
    ViewSet para Category.
    GET → público
    POST / PUT / PATCH / DELETE → apenas admin
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_permissions(self):
        # Rotas públicas (catálogo)
        if self.request.method in ["GET", "HEAD", "OPTIONS"]:
            return [AllowAny()]

        # Escrita apenas para admin
        return [IsAdminUser()]

