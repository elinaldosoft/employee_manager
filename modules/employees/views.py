from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Employee, Departament
from .serializers import EmployeeSerializer
from .forms import EmployeeForm


class EmployeeView(APIView):
    """
    Retrieve the list of Employee name
    """
    def parser_request(self, request):
        name_departament = request.data.get('departament', None)
        if name_departament:
            departament, created = Departament.objects.get_or_create(name=name_departament)
            request.data['departament'] = departament.pk
        return request.data

    def get(self, request, format=None):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        form = EmployeeForm(self.parser_request(request) or None)
        if form.is_valid():
            employee = form.save(commit=True)
            if employee:
                return Response({'name': employee.name, 'email': employee.email,
                                'departament': employee.departament.name,
                                 'created_at': employee.created_at}, status=201)
        else:
            return Response(dict(form.errors.items()), status=400)

    def delete(self, request):
        if "email" in request.data:
            email = request.data.get("email")
            employee = Employee.objects.filter(email=email)
            if employee:
                employee.delete()
                return Response("ok", status=200)
            else:
                return Response({'error': 'Email inexistente'}, status=400)
        else:
            return Response({'error': 'Você deve passar o email do funcionário'}, status=400)
