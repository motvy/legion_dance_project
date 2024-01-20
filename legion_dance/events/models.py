from django.db import models
import user_profile.models as profile_models

class Event(models.Model):
    event_name = models.CharField(max_length=128)
    event_description = models.TextField(null=True)
    author_id = models.ForeignKey(to=profile_models.User, on_delete=models.CASCADE)
    event_datetime = models.DateTimeField()

class TeamEvent(models.Model):
    team_id = models.ForeignKey(to=profile_models.Team, on_delete=models.CASCADE)
    event_id = models.ForeignKey(to=Event, on_delete=models.CASCADE)
