from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.ToDoItem)
admin.site.register(models.Chirp)
admin.site.register(models.Comment)
