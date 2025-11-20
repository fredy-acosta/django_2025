from rest_framework import serializers
from .models import tax

class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = tax
        fields = '__all__'
