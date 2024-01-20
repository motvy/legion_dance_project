from django.db import models
import user_profile.models as profile_model
import events.models as event_model
from user_profile.models import Team

import datetime

class Achievement(models.Model):
    achievement_name = models.CharField(max_length=128)
    exp_count = models.IntegerField(default=0)
    team_id = models.ForeignKey(to=Team, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.achievement_name

class UserAchievement(models.Model):
    user_id = models.ForeignKey(to=profile_model.User, on_delete=models.CASCADE)
    achievement_id = models.ForeignKey(to=Achievement, on_delete=models.CASCADE)
    event_id = models.ForeignKey(to=event_model.Event, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(auto_now_add=True)

