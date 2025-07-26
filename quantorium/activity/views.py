from django.shortcuts import render
from rest_framework import viewsets
from .models import Visit, Point
from .serializers import VisitSerializer, PointSerializer

# Create your views here.

class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer

