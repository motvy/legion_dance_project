from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def events(request):
    context = {'title': 'Calendar'}
    return render(request, 'calendar.html', context)
