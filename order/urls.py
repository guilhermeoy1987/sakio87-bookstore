#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import OrderViewSet  # já importa direto

router = DefaultRouter()
router.register(r"order", OrderViewSet, basename="order")  # corrigido aqui

urlpatterns = [
    path("", include(router.urls)),
]
