from rest_framework import serializers
from .models import Visit, Point


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'
        
        
class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ['user_id', 'group_id', 'points']