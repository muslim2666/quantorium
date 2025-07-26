from django.db import models
from users.models import Users

# Create your models here.

class Visit(models.Model):
    user_id = models.IntegerField(unique=True)
    visit_date = models.DateTimeField(auto_now_add=True)
    is_present = models.IntegerField(max_length=2)
    
    def __str__(self):
        return f'{self.user_id} + {self.visit_date} + {self.is_present}'
    
    
class Point(models.Model):
    user_id = models.IntegerField(unique=True)
    group_id = models.IntegerField(unique=True)
    points = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user_id} + {self.group_id} + {self.points}'