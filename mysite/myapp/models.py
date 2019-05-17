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

##Friend class based on this tutorial https://www.youtube.com/watch?v=IXJ46DitsIg&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj&index=55
##Friends are a one way relationship
##You can be friends with someone that isn't friends with you, and vice versa
class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE, null=True)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, old_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(old_friend)
