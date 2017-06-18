#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from .models import Departament, Employee
from django.db.models import F

__author__ = '@elinaldosoft'


@receiver(post_save, sender=Employee)
def after_count_number_employee_in_departament(sender, update_fields, created, instance, **kwargs):
    if created:
        Departament.objects.filter(pk=instance.departament.pk).update(count_employee=F('count_employee') + 1)


@receiver(pre_save, sender=Employee)
def before_count_number_employee_in_departament(sender, update_fields, instance, **kwargs):
    if instance.pk:
        obj = Employee.objects.get(pk=instance.pk)
        if obj.departament != instance.departament:
            Departament.objects.filter(pk=obj.departament.pk).update(count_employee=F('count_employee') - 1)
            Departament.objects.filter(pk=instance.departament.pk).update(count_employee=F('count_employee') + 1)


@receiver(post_delete, sender=Employee)
def decrement_count_number_employee_in_departament(sender, instance, *args, **kwargs):
    Departament.objects.filter(pk=instance.departament.pk).update(count_employee=F('count_employee') - 1)
