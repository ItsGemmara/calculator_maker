from rest_framework import fields, serializers

from .models import Calculator, VARIABLE_CHOICES
from .validators import FormulaValidators


class FormulaSerializer(serializers.ModelSerializer):

    variables = fields.MultipleChoiceField(choices=VARIABLE_CHOICES)

    def validate(self, validated_data):
        raw_formula = validated_data['formula']
        formula_validators = FormulaValidators()
        validated_formula = formula_validators.create_formula(raw_formula)
        validated_data['formula'] = validated_formula
        return validated_data

    class Meta:
        model = Calculator
        fields = ("name", "formula", "description", "variables")


class CalculatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calculator
        fields = ("name", "formula", "description", "variables", 'pk')


class PreCalculateSerializer(serializers.Serializer):
    name = serializers.CharField()


