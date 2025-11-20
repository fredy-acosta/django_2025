from rest_framework import serializers
from .models import branch

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = branch
        fields = '__all__'
