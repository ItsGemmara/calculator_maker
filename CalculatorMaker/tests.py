from rest_framework.test import APITestCase
from rest_framework import status

from .validators import FormulaValidators
from .models import Calculator
from .serializer import CalculatorSerializer


class CreatCalculatorTestCase(APITestCase):

    def setUp(self):
        self.data = {"name": 'test_name', "formula": '89655/8', "description": 'test description',
                "variables": ['a', 'b', 'c']}

    def test_create(self):
        response = self.client.post("/api/calculator-viewset//", self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class CalculatorTestCase(APITestCase):

    def setUp(self):
        self.calculator = Calculator.objects.create(name='test_name', formula='89655/8', description='test description',
                                                    variables=['a', 'b', 'c'])
        self.data = CalculatorSerializer(self.calculator).data

    def test_patch_calculator(self):
        self.data.update({'name': 'Changed_name'})
        response = self.client.patch(f'/api/calculator-viewset//{self.calculator.id}/', self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_calculator(self):
        self.data.update({"name": 'Changed_name', "formula": '655/8', "Changed_description": 'Changed test description',
                "variables": ['a', 'b', 'c']})
        response = self.client.put(f'/api/calculator-viewset//{self.calculator.id}/', self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_calculator(self):
        response = self.client.delete(f'/api/calculator-viewset//{self.calculator.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_read_calculator_list(self):
        response = self.client.get('/api/calculator-viewset//')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_calculator_detail(self):
        response = self.client.get('/api/calculator-viewset//')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class FormulaValidationTestCase(APITestCase):

    def setUp(self):
        self.formula_validators = FormulaValidators()

    def test_zero_division(self):
        self.assertRaises(ZeroDivisionError, self.formula_validators.division_validators, '587/0')

    def test_no_num_division(self):
        self.assertRaisesMessage(ValueError, 'This error occurs when you try to divide anything other than numbers',
                                 self.formula_validators.division_validators, '587/h')
        self.assertRaisesMessage(ValueError, 'This error occurs when you try to divide anything other than numbers',
                                 self.formula_validators.division_validators, 'f/8')


