from django.urls import path
from user_profile.views import profile, login, signup

app_name = 'user_profile'

urlpatterns = [
   path('', profile, name='index'),
   path('login/', login, name='login'),
   path('signup/', signup, name='signup'),
]