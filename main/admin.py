from django.contrib import admin

from .models import Task, RegistrationModel

# Register your models here.
admin.site.register(Task)
admin.site.register(RegistrationModel)