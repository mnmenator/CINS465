from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chirp(models.Model):
    chirp_field = models.CharField(max_length=240)
    chirp_author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.chirp_field

class Comment(models.Model):
    comment_field = models.CharField(max_length=240)
    comment_chirp = models.ForeignKey(Chirp, on_delete=models.CASCADE)
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.comment_field)
