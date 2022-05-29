from rest_framework import fields, serializers

from .models import Calculator, VARIABLE_CHOICES
from .validators import formula_validators


class CalculatorSerializer(serializers.ModelSerializer):

    variables = fields.MultipleChoiceField(choices=VARIABLE_CHOICES)

    def validate(self, validated_data):
        raw_formula = validated_data['formula']
        validated_formula = formula_validators(raw_formula)
        return validated_data

    class Meta:
        model = Calculator
        fields = ("name", "formula", "description", "variables")

