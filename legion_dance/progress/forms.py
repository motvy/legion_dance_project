from django import forms

from progress.models import Achievement, UserAchievement
from user_profile.models import Team, User

class AchievementCreationForm(forms.ModelForm):
    achievement_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "",
        'id': 'achievement_name',
        'class': 'profile_input_field',
    }))

    exp_count = forms.IntegerField(max_value=100, min_value=1, widget=forms.TextInput(attrs={
        'placeholder': "",
        'id': 'exp_count',
        'class': 'profile_input_field'
    }))

    team_id = forms.ModelChoiceField(queryset=Team.objects.all(), empty_label="", widget=forms.Select(attrs={
        'placeholder': "",
        'id': 'team',
        'class': 'profile_input_field',
        'readonly': 'readonly'
    }))

    class Meta:
        model = Achievement
        fields = ('achievement_name', 'exp_count', 'team_id')

class UserAchievementCreationForm(forms.ModelForm):
    user_id = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="", widget=forms.Select(attrs={
        'placeholder': "User",
        'id': 'user_id',
        'class': 'profile_input_field'
    }))

    achievement_id = forms.ModelChoiceField(queryset=Achievement.objects.all(), empty_label="", widget=forms.Select(attrs={
        'placeholder': "Aciev",
        'id': 'achievement_id',
        'class': 'profile_input_field'
    }))

    class Meta:
        model = UserAchievement
        fields = ('user_id', 'achievement_id')