from rest_framework.decorators import permission_classes
from rest_framework.serializers import Serializer
from patients.models import Patient
from rest_framework import viewsets, permissions
from .serializers import PatientSerializer

#viewset
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PatientSerializer