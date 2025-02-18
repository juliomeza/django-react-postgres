from rest_framework import serializers
from .models import Enterprise, Client, Project

class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    enterprise = EnterpriseSerializer(read_only=True)
    enterprise_id = serializers.PrimaryKeyRelatedField(
        queryset=Enterprise.objects.all(), source='enterprise', write_only=True
    )
    
    class Meta:
        model = Client
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    client_id = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), source='client', write_only=True
    )
    
    class Meta:
        model = Project
        fields = '__all__'
