from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .api import FormulaMakerAPI, CalculatorMakerApi


calculator_router = DefaultRouter()
calculator_router.register(r'calculator-viewset/', CalculatorMakerApi, basename='calculator')

formula_router = DefaultRouter()
formula_router.register(r'formula-viewset/', FormulaMakerAPI, basename='formula')

urlpatterns = [
    path('', include(formula_router.urls)),
    path('calculator/', include(calculator_router.urls)),

]
