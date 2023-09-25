from django.urls import path
from messenger.views import messenger

app_name = 'messenger'

urlpatterns = [
   path('', messenger, name='index')
]