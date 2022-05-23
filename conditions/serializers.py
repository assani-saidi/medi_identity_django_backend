from rest_framework import serializers
from conditions.models import Condition

# lead serializer
class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = '__all__'