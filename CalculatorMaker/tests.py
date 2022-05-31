from rest_framework.test import APITestCase, APITransactionTestCase, APIClient, APIRequestFactory
from rest_framework import status

from .validators import FormulaValidators, RawFormulaValidators
from .models import Calculator
from .serializer import CalculatorSerializer
from .api import CalculatorMakerApi


class CreatCalculatorTestCase(APITestCase):

    def setUp(self):
        self.data = {"name": 'test_name', "formula": '89655/8', "description": 'test description',
                "variables": ['a', 'b', 'c']}

    def test_create(self):
        response = self.client.post("/api/formula-viewset//", self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class CalculatorTestCase(APITestCase):

    def setUp(self):
        self.calculator = Calculator.objects.create(name='test_name', formula='89655/8', description='test description',
                                                    variables=['a', 'b', 'c'])
        self.data = CalculatorSerializer(self.calculator).data

    def test_patch_calculator(self):
        self.data.update({'name': 'Changed_name'})
        response = self.client.patch(f'/api/formula-viewset//{self.calculator.id}/', self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_calculator(self):
        self.data.update({"name": 'Changed_name', "formula": '655/8', "Changed_description": 'Changed test description',
                "variables": ['a', 'b', 'c']})
        response = self.client.put(f'/api/formula-viewset//{self.calculator.id}/', self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_calculator(self):
        response = self.client.delete(f'/api/formula-viewset//{self.calculator.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_read_calculator_list(self):
        response = self.client.get('/api/formula-viewset//')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_calculator_detail(self):
        response = self.client.get('/api/formula-viewset//')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class FormulaValidationTestCase(APITestCase):

    def setUp(self):
        self.formula_validators = RawFormulaValidators()

    def test_zero_division(self):
        self.assertRaises(ZeroDivisionError, self.formula_validators.division_validators, '587/0')

    def test_no_num_division(self):
        self.assertRaisesMessage(ValueError, 'This error occurs when you try to divide anything other than numbers',
                                 self.formula_validators.division_validators, '587/h')
        self.assertRaisesMessage(ValueError, 'This error occurs when you try to divide anything other than numbers',
                                 self.formula_validators.division_validators, 'f/8')


class ModelTestCase(APITransactionTestCase):

    reset_sequences = True

    def test_calculator(self):
        obj = Calculator.objects.create(name='test_name', formula='2/5', description= 'dis', variables=['a','b'])
        self.assertEqual(1, obj.pk)  # database test
        self.assertEqual('dis', obj.description)  # database test
        self.assertEqual(['a','b'], obj.variables)  # database test
        self.assertEqual('2/5', obj.formula)
# -------------------------------------------------------------------------------------------------------------------

class CalculatorIntegrationTest(APITestCase):

    def setUp(self):
        self.data = {"name": 'test_name', "formula": '896/8', "description": 'test description',
                     "variables": ['a', 'b', 'c']}
        create_response = self.client.post("/api/formula-viewset//", self.data)


    def test_calculator_maker_formula_maker(self):
        client = APIClient()
        formula_response = client.get('/api/formula-viewset//', format='api')
        formula_data = formula_response.data[0]
        calculator_response = client.post('/api/calculator/calculator-viewset//get_formula/', data={'name': formula_data['name']})
        self.assertEqual(len(formula_response.data), 1)
        self.assertEqual(formula_response.status_code, status.HTTP_200_OK)
        self.assertEqual(calculator_response.data['formula'], formula_data['formula'])
        self.assertEqual(calculator_response.data['variables'], (formula_data['variables']))


#------------------------------------------------------------------------------------------------------------








