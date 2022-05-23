from rest_framework import serializers
from records.models import Record

# lead serializer
class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'