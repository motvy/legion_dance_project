from django.db import models
from django.contrib.auth.models import AbstractUser

class Team(models.Model):
    team_name = models.CharField(max_length=128, unique=True)
    team_logo = models.ImageField(upload_to='team_images', null=True, blank=True)
    
    def __str__(self):
        return self.team_name

class User(AbstractUser):  
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    team_id = models.ForeignKey(to=Team, on_delete=models.PROTECT, null=True)
    is_teacher = models.BooleanField(default=False)
    exp = models.IntegerField(default=0)
