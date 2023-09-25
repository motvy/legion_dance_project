from django.shortcuts import render

def messenger(request):
    context = {'title': 'Messenger'}
    return render(request, 'messenger.html', context)
