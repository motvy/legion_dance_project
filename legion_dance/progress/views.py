from django.shortcuts import render


def progress(request):
    context = {'title': 'Progress'}
    return render(request, 'progress.html', context)
