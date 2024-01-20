from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from user_profile.models import User, Team


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Nickname",
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


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Nickname",
        'id': 'username',
        'class': 'input-field',
        'autocomplete': 'off'
    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "First Name",
        'id': 'first_name',
        'class': 'input-field'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Last Name",
        'id': 'last_name',
        'class': 'input-field'
    }))

    team_id = forms.ModelChoiceField(queryset=Team.objects.all(), empty_label="", widget=forms.Select(attrs={
        'placeholder': "Team",
        'id': 'team',
        'class': 'input-field'
    }))

    # team = forms.CharField(widget=forms.TextInput(attrs={
    #     'placeholder': "Team",
    #     'id': 'team',
    #     'class': 'input-field'
    # }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': "Email",
        'id': 'email',
        'class': 'input-field'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'id': 'password1',
        'class': 'input-field'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat Password',
        'id': 'password2',
        'class': 'input-field'
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'team_id', 'email', 'password1', 'password2')

class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Nickname",
        'id': 'username',
        'class': 'username_input_field',
        'readonly': 'readonly'
    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "First Name",
        'id': 'first_name',
        'class': 'profile_input_field'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Last Name",
        'id': 'last_name',
        'class': 'profile_input_field'
    }))

    # team = forms.CharField(widget=forms.TextInput(attrs={
    #     'placeholder': "Team",
    #     'id': 'team',
    #     'class': 'profile_input_field',
    #     'readonly': 'readonly'
    # }))
    # team = forms.ModelChoiceField(queryset=Team.objects.all(), widget=forms.Select(attrs={
    #     'placeholder': "Team",
    #     'id': 'team',
    #     'class': 'profile_input_field',
    #     'readonly': 'readonly'
    # }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': "Email",
        'id': 'email',
        'class': 'profile_input_field',
        'readonly': 'readonly'
    }))

    image = forms.ImageField(widget=forms.FileInput(attrs={
        'id': 'image',
        'class': 'img_profile_label',
    }), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'image')

