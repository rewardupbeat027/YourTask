from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.CharField(blank=True, max_length=100)
    completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registration_task')

class RegistrationModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='registration')
    code_word = models.TextField('Кодовое слово:', max_length=20, blank=True)