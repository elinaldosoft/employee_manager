from modules.base_model import TimeStamp
from django.db import models
from django.utils.translation import ugettext as _


class Departament(TimeStamp):
    name = models.CharField(max_length=200, unique=True, verbose_name=_('name'))
    description = models.TextField(null=True, blank=True, verbose_name=_('description'))
    count_employee = models.PositiveIntegerField(default=0, editable=False, verbose_name=_('Quantidade de Funcionários'))

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ('-created_at', )
        db_table = 'departaments'

    def __str__(self):
        return self.name


class Employee(TimeStamp):
    name = models.CharField(max_length=200, unique=True, verbose_name=_('name'))
    email = models.EmailField(unique=True)
    departament = models.ForeignKey(Departament, related_name='employee_departament_set')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
        ordering = ('-created_at', )
        db_table = 'employees'

    def __str__(self):
        return self.name
