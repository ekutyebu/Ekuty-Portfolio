from rest_framework import serializers
from .models import Message, Works

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class WorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Works
        fields = '__all__'