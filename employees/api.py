from rest_framework.decorators import permission_classes
from rest_framework.serializers import Serializer
from employees.models import Employee
from rest_framework import viewsets, permissions
from .serializers import EmployeeSerializer

#viewset
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EmployeeSerializer