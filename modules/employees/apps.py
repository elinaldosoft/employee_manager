from django.apps import AppConfig


class EmployeesConfig(AppConfig):
    name = 'modules.employees'
    verbose_name = 'Gerenciamento de Funcionários'

    def ready(self):
        from . import signals
