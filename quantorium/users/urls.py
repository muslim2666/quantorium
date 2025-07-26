from django.urls import path
from .views import UserListView
from .views import GroupListView
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/api/users', UserListView.as_view(), name='user-list'),
    path('v1/api/groups', GroupListView.as_view(), name='groups-list'),

]