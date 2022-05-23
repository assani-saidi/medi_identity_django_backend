from rest_framework import serializers
from employees.models import Employee

# lead serializer
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'