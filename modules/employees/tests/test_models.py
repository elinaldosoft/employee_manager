from django.test import TestCase
from modules.employees.models import Departament, Employee


class DepartamentTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Departament.objects.create(name="Tecnologia", count_employee=2, description="Description of test")

    def test_name_label(self):
        departament = Departament.objects.get(pk=1)
        field_label = departament._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'nome')

    def test_description_label(self):
        departament = Departament.objects.get(pk=1)
        field_label = departament._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_count_employee_label(self):
        departament = Departament.objects.get(pk=1)
        field_label = departament._meta.get_field('count_employee').verbose_name
        self.assertEquals(field_label, 'Quantidade de Funcionários')

    def test_name_max_length(self):
        departament = Departament.objects.get(pk=1)
        max_length = departament._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_count_employee_editable(self):
        departament = Departament.objects.get(pk=1)
        editable = departament._meta.get_field('count_employee').editable
        self.assertFalse(editable)


class EmployeeTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        departament = Departament.objects.create(name="Tecnologia", count_employee=0, description="Description of test")
        Employee.objects.create(
            name="Elinaldo do Nascimento Monteiro",
            email="elinaldo.java@gmail.com",
            departament=departament
        )

    def test_name_label(self):
        employee = Employee.objects.get(pk=1)
        field_label = employee._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'nome')

    def test_name_type_unique(self):
        employee = Employee.objects.get(pk=1)
        type_unique = employee._meta.get_field('name').unique
        self.assertTrue(type_unique)

    def test_increment_departament(self):
        employee = Employee.objects.get(pk=1)
        self.assertEqual(employee.departament.count_employee, 1)

    def test_decrement_departament(self):
        Employee.objects.get(pk=1).delete()
        departament = Departament.objects.get(pk=1)
        self.assertEqual(departament.count_employee, 0)

    def test_update_departament_employee_decrement(self):
        departament = Departament.objects.create(name="Administração", count_employee=0, description="Description of test")
        employee = Employee.objects.get(pk=1)
        employee.departament = departament
        employee.save()

        self.assertEqual(employee.departament.name, 'Administração')
