from rest_framework import serializers
from .models import Enterprise, Owner, Project

class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        fields = '__all__'

class OwnerSerializer(serializers.ModelSerializer):
    enterprise = EnterpriseSerializer(read_only=True)
    enterprise_id = serializers.PrimaryKeyRelatedField(
        queryset=Enterprise.objects.all(), source='enterprise', write_only=True
    )
    
    class Meta:
        model = Owner
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    enterprise = EnterpriseSerializer(read_only=True)
    enterprise_id = serializers.PrimaryKeyRelatedField(
        queryset=Enterprise.objects.all(), source='enterprise', write_only=True
    )
    
    class Meta:
        model = Project
        fields = '__all__'
