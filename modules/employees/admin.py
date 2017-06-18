from django.contrib import admin
from django.forms import ModelForm
from django_select2.forms import ModelSelect2Widget
from .models import Employee, Departament
from .widgets import Bootstrap4Select


class DepartamentSelect2Widget(Bootstrap4Select, ModelSelect2Widget):
    search_fields = [
        'name__icontains',
    ]


class EmployeeForm(ModelForm):
    class Meta:
        widgets = {
            'departament': DepartamentSelect2Widget()
        }


@admin.register(Departament)
class DepartamentAdmin(admin.ModelAdmin):
    readonly_fields = ['count_employee']
    list_display = ['name', 'count_employee_human']

    def count_employee_human(self, obj):
        return obj.count_employee

    count_employee_human.short_description = "Quantidade de Funcionários"


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeForm
    list_display = ['name', 'email', 'departament']
    search_fields = ['name',  'email', 'departament']
    list_filter = ['departament']
