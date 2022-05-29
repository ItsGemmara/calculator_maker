import json

from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Calculator
from .serializer import CalculatorSerializer


class FormulaValidationTestCase(APITestCase):

    def test_zero_division(self):
        data = {"name": 'test_name', "formula": '5/2', "description": 'test description', "variables": ['a', 'b', 'c']}
        response = self.client.post("/api/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)