from django.shortcuts import render, HttpResponsePermanentRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from user_profile.models import User, Team
from progress.models import UserAchievement, Achievement
from progress.forms import AchievementCreationForm, UserAchievementCreationForm

@login_required
def progress(request):
    if request.user.is_teacher:
        return HttpResponsePermanentRedirect(reverse('progress:total'))
    else:
        context = {
            'title': 'Progress',
            'achievs': UserAchievement.objects.select_related('achievement_id').filter(user_id=request.user).order_by('date').reverse()
        }

        return render(request, 'progress.html', context)

@login_required
def total_progress(request):
    context = {
        'title': 'Progress',
        'users': User.objects.filter(team_id=request.user.team_id, is_teacher=False).order_by('exp').values().reverse(),
    }

    return render(request, 'total_progress.html', context)

@login_required
def achiev_edit(request):
    if request.user.is_teacher:
        errors = ''
        if request.method == 'POST':
            updated_request = request.POST.copy()
            updated_request.update({'create-team_id': request.user.team_id})
            createAchievForm = AchievementCreationForm(updated_request, prefix='create')
            if createAchievForm.is_valid():
                createAchievForm.save()
                return HttpResponsePermanentRedirect(reverse('progress:achiev_edit'))
            else:
                print('Invalid')
                print(createAchievForm.errors.as_text())
                errors=createAchievForm.errors.as_text()
        else:
            createAchievForm = AchievementCreationForm(prefix='create')

        if request.method == 'GET':
            for a_id in request.GET.getlist('selection'):
                achiev = Achievement.objects.get(id=a_id)

                for user in UserAchievement.objects.filter(achievement_id=a_id):
                    u = User.objects.get(id=user.user_id.id)
                    u.exp = u.exp - achiev.exp_count
                    u.save()

                achiev.delete()

        context = {'title': 'Progress',
                'createAchievForm': createAchievForm,
                'errors': ':'.join( errors.split('\n')).replace('*', '').replace('  ', ' '),
                'achievs': Achievement.objects.filter(team_id=request.user.team_id),
        }

        return render(request, 'achiev_edit.html', context)

    else:
        return HttpResponsePermanentRedirect(reverse('progress:total'))

@login_required
def progress_edit(request):
    if request.user.is_teacher:
        errors = ''
        if request.method == 'POST':
            # updated_request = request.POST.copy()
            # updated_request.update({'create-team_id': request.user.team_id})
            createAchievForm = UserAchievementCreationForm(request.POST, prefix='create')
            if createAchievForm.is_valid():
                u_id = createAchievForm.data['create-user_id']
                a_id = createAchievForm.data['create-achievement_id']
                user = User.objects.get(id=u_id)
                achiev = Achievement.objects.get(id=a_id)
                user.exp = user.exp + achiev.exp_count
                user.save()

                createAchievForm.save()
                return HttpResponsePermanentRedirect(reverse('progress:progress_edit'))
            else:
                print('Invalid')
                print(createAchievForm.errors.as_text())
                errors=createAchievForm.errors.as_text()
        else:
            createAchievForm = UserAchievementCreationForm(prefix='create', )

        if request.method == 'GET':
            print(request.GET.getlist('selection'))
            for my_id in request.GET.getlist('selection'):
                au_id, a_id, u_id = my_id.split('_')
                user_achiev = UserAchievement.objects.get(id=au_id)
                user = User.objects.get(id=u_id)
                achiev = Achievement.objects.get(id=a_id)

                user.exp = user.exp - achiev.exp_count
                user.save()
                user_achiev.delete()

        context = {'title': 'Progress',
                'createAchievForm': createAchievForm,
                'errors': ':'.join( errors.split('\n')).replace('*', '').replace('  ', ' '),

                    # UserAchievement.objects.select_related('achievement_id').filter(user_id=request.user).order_by('date').reverse()
                'achievs': UserAchievement.objects.select_related('user_id').order_by('user_id')
        }

        return render(request, 'progress_edit.html', context)

    else:
        return HttpResponsePermanentRedirect(reverse('progress:total'))