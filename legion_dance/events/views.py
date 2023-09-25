from django.shortcuts import render


def events(request):
    context = {'title': 'Calendar'}
    return render(request, 'calendar.html', context)
