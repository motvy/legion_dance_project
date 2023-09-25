from django.urls import path
from events.views import events

app_name = 'events'

urlpatterns = [
   path('', events, name='index')
]
