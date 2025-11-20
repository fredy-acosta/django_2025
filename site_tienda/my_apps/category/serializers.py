from rest_framework import serializers
from .models import category   # ajusta al nombre real

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
