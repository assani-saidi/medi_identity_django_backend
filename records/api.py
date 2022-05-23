from rest_framework.decorators import permission_classes
from rest_framework.serializers import Serializer
from records.models import Record
from rest_framework import viewsets, permissions
from .serializers import RecordSerializer

#viewset
class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RecordSerializer