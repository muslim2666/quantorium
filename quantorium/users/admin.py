from django.contrib import admin
from .models import Group
from .models import Users

# Register your models here.
admin.site.register(Users)
admin.site.register(Group)
