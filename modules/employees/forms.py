#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import Employee

__author__ = '@elinaldosoft'


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'departament']
