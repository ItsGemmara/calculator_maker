from rest_framework.response import Response
from rest_framework import generics, mixins, views
from rest_framework.decorators import action
from rest_framework import viewsets

from .models import Calculator
from .serializer import CalculatorSerializer


class CalculatorMakerAPI(viewsets.ModelViewSet):

    queryset = Calculator.objects.all()
    serializer_class = CalculatorSerializer

    # @action(detail=False, methods=['post', ])
    # def create_formula(self, a):
    #     obj = Calculator.objects.
    #     return Response({"formula": 1}, status=200)
