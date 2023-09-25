from django.shortcuts import render

def profile(request):
    context = {'title': 'Profile'}
    return render(request, 'profile.html', context)
