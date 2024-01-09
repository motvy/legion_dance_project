from django.shortcuts import render, HttpResponsePermanentRedirect
from django.contrib import auth
from django.urls import reverse

from user_profile.forms import UserLoginForm


def profile(request):
    context = {'title': 'Profile'}
    return render(request, 'profile.html', context)

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponsePermanentRedirect(reverse('profile:index'))
    else:
        form = UserLoginForm()
    context = {'title': 'Login', 'form': UserLoginForm()}
    return render(request, 'login.html', context)

def signup(request):
    context = {'title': 'SignUp'}
    return render(request, 'signup.html', context)