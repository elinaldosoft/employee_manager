#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import EmployeeView

__author__ = '@elinaldosoft'

urlpatterns = [
    url(r'$', EmployeeView.as_view(), name='list'),
    url(r'add$', EmployeeView.as_view(), name='add'),
    url(r'del$', EmployeeView.as_view(), name='delete'),
]
