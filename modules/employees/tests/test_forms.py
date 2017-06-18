#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.test import TestCase
from modules.employees.forms import EmployeeForm
from modules.employees.models import Departament, Employee

__author__ = '@elinaldosoft'


class EmployeeFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        departament = Departament.objects.create(name="Tecnologia", count_employee=2, description="Description of test")
        Employee.objects.create(
            name="Elinaldo Monteiro",
            email="elinaldo.up@gmail.com",
            departament=departament
        )

    def test_valid_form(self):
        data = {'name': 'elinaldo', 'email': 'elinaldo.java@gmail.com', 'departament': 1}
        form = EmployeeForm(data=data)
        self.assertTrue(form.is_valid())

    def test_valid_form_missing_name(self):
        data = {'email': 'elinaldo.java@gmail.com', 'departament': 1}
        form = EmployeeForm(data=data)
        self.assertEqual({'name': ['Este campo é obrigatório.']}, dict(form.errors.items()))

    def test_valid_form_missing_email(self):
        data = {'name': 'elinaldo', 'departament': 1}
        form = EmployeeForm(data=data)
        self.assertEqual({'email': ['Este campo é obrigatório.']}, dict(form.errors.items()))

    def test_valid_form_missing_departament(self):
        data = {'name': 'elinaldo', 'email': 'elinaldo.java@gmail.com'}
        form = EmployeeForm(data=data)
        self.assertEqual({'departament': ['Este campo é obrigatório.']}, dict(form.errors.items()))

    def test_valid_form_format_data_departament(self):
        data = {'name': 'elinaldo', 'email': 'elinaldo.java@gmail.com', 'departament': 'tecnologia'}
        form = EmployeeForm(data=data)
        self.assertEqual({'departament': ['Faça uma escolha válida. Sua escolha não é uma das disponíveis.']}, dict(form.errors.items()))

    def test_create_object_by_form(self):
        data = {'name': 'elinaldo', 'email': 'elinaldo.java@gmail.com', 'departament': 1}
        form = EmployeeForm(data=data)
        obj = form.save(commit=True)
        self.assertEqual(obj.pk, 2)

    def test_valid_email_unique(self):
        data = {'name': 'Jonh elinaldo', 'email': 'elinaldo.up@gmail.com', 'departament': 1}
        form = EmployeeForm(data=data)
        self.assertEqual({'email': ['Funcionário com este Email já existe.']}, dict(form.errors.items()))

    def test_valid_name_unique(self):
        data = {'name': 'Elinaldo Monteiro', 'email': 'elinaldo@gmail.com', 'departament': 1}
        form = EmployeeForm(data=data)
        self.assertEqual({'name': ['Funcionário com este Nome já existe.']}, dict(form.errors.items()))
