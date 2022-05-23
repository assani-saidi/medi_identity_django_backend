from rest_framework import serializers
from patients.models import Patient
from drf_extra_fields.fields import Base64ImageField

# lead serializer
class PatientSerializer(serializers.ModelSerializer):
    image = Base64ImageField()
    class Meta:
        model = Patient
        fields = '__all__'