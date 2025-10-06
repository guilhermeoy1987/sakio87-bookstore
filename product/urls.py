from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import CategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register(r"category", CategoryViewSet, basename="category")
router.register(r"product", ProductViewSet, basename="product")

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
