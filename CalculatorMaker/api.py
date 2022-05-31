from rest_framework.response import Response
from rest_framework import generics, mixins, views
from rest_framework.decorators import action
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from .models import Calculator
from .serializer import CalculatorSerializer, FormulaSerializer, PreCalculateSerializer


class FormulaMakerAPI(viewsets.ModelViewSet):

    queryset = Calculator.objects.all()
    serializer_class = FormulaSerializer

    @action(detail=False, methods=['post', ])
    def create_formula(self, a):
        return Response({"formula": 1}, status=200)


class CalculatorMakerApi(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):

    queryset = Calculator.objects.all()
    serializer_class = CalculatorSerializer

    def get_serializer_class(self):
        if self.action == 'get_formula':
            return PreCalculateSerializer
        else:
            return CalculatorSerializer
        # elif self.action == 'calculate':
        #     return CalculateSerializer

    @action(detail=False, methods=['post', ])
    def get_formula(self, a):
        serializer = PreCalculateSerializer(data=self.request.data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data["name"]
        obj = get_object_or_404(Calculator, name=name)
        variables = obj.variables
        formula = obj.formula
        return Response({'variables': set(variables), 'formula': formula}, status=200)

    # @action(detail=False, methods=['post', ])
    # def calculate(self, a, name):

    #     serializer = CalculatorSerializer(data=self.request.data)
    #     serializer.is_valid(raise_exception=True)
    #     return Response({'pk': variables}, status=200)
