from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Group



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
        
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['group_name', 'teacher_name']
        