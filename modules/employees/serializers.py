#!/usr/bin/python
# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Employee, Departament

__author__ = '@elinaldosoft'


class DepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departament
        fields = ('name', 'description', 'count_employee')


class EmployeeSerializer(serializers.ModelSerializer):
    """Serialize the information of a Employee model"""
    departament = serializers.PrimaryKeyRelatedField(read_only=True, source='departament.name')

    class Meta:
        model = Employee
        fields = ('name', 'email', 'departament')
