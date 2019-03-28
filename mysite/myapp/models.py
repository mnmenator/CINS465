from django.db import models

# Create your models here.
class ToDoItem(models.Model):
    todo_field = models.CharField(max_length=240)

    def __str__(self):
        return self.todo_field

class ChirpItem(models.Model):
    chirp_field = models.CharField(max_length=240)

    def __str__(self):
        return self.chirp_field
