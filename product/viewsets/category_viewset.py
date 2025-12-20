from rest_framework import viewsets
from product.models import Category
from product.serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CategoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet para Category.
    Suporta: list, retrieve, create, update, destroy
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [] 
