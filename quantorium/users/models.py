from django.db import models

# Create your models here.
class Users(models.Model):
    last_name = models.CharField(max_length=25, verbose_name="Фамилия")
    first_name = models.CharField(max_length=25, verbose_name="Имя")
    middle_name = models.CharField(max_length=25, verbose_name="Отчесво")
    label = models.CharField(max_length=20, verbose_name="Ник")
    level = models.CharField(max_length=3, verbose_name="Класс")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.middle_name
    
    
    
class Group(models.Model):
    group_name = models.CharField(max_length=225)
    teacher_name = models.CharField(max_length=225)
    
    def __str__(self):
        return self.group_name + ' ' + self.teacher_name