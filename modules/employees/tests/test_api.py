#!/usr/bin/python
# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
import datetime
import json
from modules.employees.models import Departament, Employee

__author__ = '@elinaldosoft'


class ApiTest(APITestCase):
    url_add = reverse('employee:add')
    url_list = reverse('employee:list')
    url_delete = reverse('employee:delete')

    @classmethod
    def setUpTestData(cls):
        departament = Departament.objects.create(name="Tecnologia", count_employee=0, description="Description of test")
        Employee.objects.create(
            name="Neo",
            email="matrix@matrix.com",
            departament=departament
        )

    def test_create_employee(self):
        data = {'name': 'Jonh Wick', 'email': 'jonh.wick@gmail.com', 'departament': 'tecnologia'}
        response = self.client.post(self.url_add, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_json = json.loads(response.content)
        created_at = response_json.pop('created_at')
        self.assertTrue(datetime.datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S.%fZ'))
        self.assertEqual(response_json, data)

    def test_create_employee_valid_email(self):
        data = {'name': 'Jonh Wick', 'departament': 'tecnologia'}
        response = self.client.post(self.url_add, data, format='json')
        self.assertEqual({'email': ['Este campo é obrigatório.']}, json.loads(response.content))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_employee_valid_email_already_exist(self):
        data = {'name': 'Neo 02', 'email': 'matrix@matrix.com', 'departament': 'tecnologia'}
        response = self.client.post(self.url_add, data, format='json')
        self.assertEqual({'email': ['Funcionário com este Email já existe.']}, json.loads(response.content))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_employee(self):
        response = self.client.get(self.url_list, format='javascript')
        self.assertEqual([{'name': 'Neo',
                           'email': 'matrix@matrix.com', 'departament': 'Tecnologia'}], json.loads(response.content))

    def test_delete_employee(self):
        data = {'email': 'matrix@matrix.com'}
        response = self.client.delete(self.url_delete, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('ok', json.loads(response.content))

    def test_delete_employee_nofound(self):
        data = {'email': 'matrix@matrix.com.br'}
        response = self.client.delete(self.url_delete, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual({'error': 'Email inexistente'}, json.loads(response.content))
