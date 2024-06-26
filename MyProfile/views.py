from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

from .models import Profile
from UserSystem.models import CustomUser
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from core.models import Project

from .forms import ProfileForm


@login_required
def create_profile(request):
    if Profile.objects.filter(user_id=request.user.id).exists():
        return redirect('MyProfile:get_profile')
    if request.method == "POST":
        form = ProfileForm(request.POST)
        print('Working')
        if form.is_valid():
            profile = form.save()
            profile.user_id=request.user.id
            profile.save()
            return redirect('MyProfile:get_profile')
        else:
            # Получаем ошибки валидации
            errors = form.errors
            # Обрабатываем ошибки по необходимости
            for field, error in errors.items():
                print(f"Ошибка в поле {field}: {error}")
    else:
        form = ProfileForm()


    return render(request, 'MyProfile/create_profile.html',{'form': form})


@login_required
def get_profile(request):
    try:
        user_profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return redirect('MyProfile:create_profile')
    projects = Project.objects.filter(Q(project_authors=request.user.id) | Q(project_participants=request.user.id))

    ctx = {'first_name': user_profile.firstname,
           'last_name': user_profile.lastname,
           'sername': user_profile.sername,
           'birth_date': user_profile.birth_date,
           'email': user_profile.user.email,
           'skills': user_profile.skills,
           'extrainfo': user_profile.extrainfo,
           'contact_info': user_profile.contact_info,
           'direction': user_profile.direction,
           'graduate_date': user_profile.graduate_date,
           'status_id': str(user_profile.status_id),
           'photo': user_profile.photo,
           'job_title': user_profile.job_title,
           'department': user_profile.department,
           'company_title': user_profile.company_title,
           'company_info': user_profile.company_info,
           'company_links': user_profile.company_links,
           'links': user_profile.links,
           'contact_info': user_profile.contact_info,
           'project_list': projects
           }
    print(ctx)
    if user_profile is None:
        raise PermissionDenied()
    return render(request, 'MyProfile/main_profile.html', context=ctx)


@login_required
def delete_profile(request):
    user_profile = Profile.objects.get(user=request.user)
    user_profile.delete()
    return redirect('/news')


@login_required
def update_profile(request):
    profile  = Profile.objects.get(user=request.user)
    print(profile.birth_date)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('MyProfile:get_profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'MyProfile/update_profile.html', {'form': form})