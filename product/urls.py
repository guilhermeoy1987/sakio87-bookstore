#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path, include
from rest_framework.routers import SimpleRouter

from product.viewsets.category_viewset import CategoryViewSet
from product.viewsets.product_viewset import ProductViewSet

router = SimpleRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]
