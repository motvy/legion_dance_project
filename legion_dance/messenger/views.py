from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def messenger(request):
    context = {'title': 'Messenger'}
    return render(request, 'messenger.html', context)
