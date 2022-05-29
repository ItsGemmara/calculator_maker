from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .api import CalculatorMakerAPI


calculator_router = DefaultRouter()
calculator_router.register(r'calculator-viewset/', CalculatorMakerAPI, basename='calculator')

urlpatterns = [
    path('', include(calculator_router.urls))
]
