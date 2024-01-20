from django.shortcuts import render, HttpResponsePermanentRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from user_profile.forms import UserLoginForm, UserRegistrationForm, UserProfileForm

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponsePermanentRedirect(reverse('profile:index'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)

    context = {'title': 'Profile', 'form': form}
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

    context = {'title': 'Login', 'form': form}
    return render(request, 'login.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        print(form.data)
        if form.is_valid():
            form.save()
            return HttpResponsePermanentRedirect(reverse('profile:login'))
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()

    context = {'title': 'SignUp', 'form': form}
    return render(request, 'signup.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponsePermanentRedirect(reverse('profile:login'))
