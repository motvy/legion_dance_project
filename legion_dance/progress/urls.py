from django.urls import path
from progress.views import progress, total_progress, achiev_edit, progress_edit

app_name = 'progress'

urlpatterns = [
   path('my', progress, name='index'),
   path('', total_progress, name='total'),
   path('achiev_edit', achiev_edit, name='achiev_edit'),
   path('edit', progress_edit, name='progress_edit')
]