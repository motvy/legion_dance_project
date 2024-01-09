from django import forms
from django.contrib.auth.forms import AuthenticationForm

from user_profile.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Username",
        'id': 'username',
        'class': 'input-field'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'id': 'password',
        'class': 'input-field'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')