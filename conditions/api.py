from rest_framework.decorators import permission_classes
from rest_framework.serializers import Serializer
from conditions.models import Condition
from rest_framework import viewsets, permissions
from .serializers import ConditionSerializer

#viewset
class ConditionViewSet(viewsets.ModelViewSet):
    queryset = Condition.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ConditionSerializer