from django.db import models
import user_profile.models as profile_models


class Chat(models.Model):
    chat_name = models.CharField(max_length=128)
    chat_icon = models.ImageField(upload_to='chat_images', null=True, blank=True)

class Message(models.Model):
    body = models.TextField()
    datetime = models.DateTimeField()
    user_id = models.ForeignKey(to=profile_models.User, on_delete=models.PROTECT)
    chat_id = models.ForeignKey(to=Chat, on_delete=models.PROTECT)
