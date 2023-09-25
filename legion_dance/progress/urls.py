from django.urls import path
from progress.views import progress

app_name = 'progress'

urlpatterns = [
   path('', progress, name='index')
]