from django.shortcuts import render

from rest_framework.generics import ListAPIView
from .models import Users, Group  
from .serializers import UserSerializer, GroupSerializer

class UserListView(ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    
    
class GroupListView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer