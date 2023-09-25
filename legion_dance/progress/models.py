from django.db import models
import user_profile.models as profile_model
import events.models as event_model

class Achievement(models.Model):
    achievement_name = models.CharField(max_length=128)
    exp_count = models.IntegerField(default=0)

class UserAchievement(models.Model):
    user_id = models.ForeignKey(to=profile_model.User, on_delete=models.PROTECT)
    achievement_id = models.ForeignKey(to=Achievement, on_delete=models.PROTECT)
    event_id = models.ForeignKey(to=event_model.Event, on_delete=models.PROTECT, null=True)


