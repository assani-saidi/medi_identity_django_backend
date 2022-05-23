from rest_framework.decorators import permission_classes
from rest_framework.serializers import Serializer
from providers.models import Provider
from rest_framework import viewsets, permissions
from .serializers import ProviderSerializer

#viewset
class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProviderSerializer