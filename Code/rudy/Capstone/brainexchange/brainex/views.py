from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import Skill, UserSkill


def index(request):
    return render(request, 'brainex/home.html', {})


def login_user(request):
    login_text = request.POST['login_text']
    password_text = request.POST['password_text']
    user = authenticate(request, username=login_text, password=password_text)
    print(user)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('brainex:profile'))
    else:
        return HttpResponseRedirect(reverse('brainex:index'))


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('brainex:index'))


def registration(request):
    skills = Skill.objects.all()
    skill_list = {'skills':[]}
    for skill in skills:
        skill_list['skills'].append({'id':skill.id, 'name':skill.skill_name})
    return render(request, 'brainex/registration.html', skill_list)


def create_user(request):
    new_username = request.POST['new_username']
    new_password = request.POST['new_password']
    new_first = request.POST['new_first']
    new_last = request.POST['new_last']
    new_email = request.POST['new_email']
    user = User.objects.create_user(username=new_username,
                                    password=new_password,
                                    email=new_email,
                                    first_name=new_first,
                                    last_name=new_last)

    learn_skill_1 = request.POST['learn_skill_1']
    learn_skill_2 = request.POST['learn_skill_2']
    learn_skill_3 = request.POST['learn_skill_3']
    teach_skill_1 = request.POST['teach_skill_1']
    teach_skill_2 = request.POST['teach_skill_2']
    teach_skill_3 = request.POST['teach_skill_3']

    # user.userskill_set.create

    user_skill_1 = UserSkill(fk_user=user, fk_skill=Skill.objects.get(pk=learn_skill_1), teach_boolean=False)
    user_skill_1.save()
    user_skill_2 = UserSkill(fk_user=user, fk_skill=Skill.objects.get(pk=learn_skill_2), teach_boolean=False)
    user_skill_2.save()
    user_skill_3 = UserSkill(fk_user=user, fk_skill=Skill.objects.get(pk=learn_skill_3), teach_boolean=False)
    user_skill_3.save()
    user_skill_1 = UserSkill(fk_user=user, fk_skill=Skill.objects.get(pk=teach_skill_1), teach_boolean=True)
    user_skill_1.save()
    user_skill_2 = UserSkill(fk_user=user, fk_skill=Skill.objects.get(pk=teach_skill_2), teach_boolean=True)
    user_skill_2.save()
    user_skill_3 = UserSkill(fk_user=user, fk_skill=Skill.objects.get(pk=teach_skill_3), teach_boolean=True)
    user_skill_3.save()

    return HttpResponseRedirect(reverse('brainex:profile'))


def get_user_data(request):
    print(request.user.userskill_set)
    return HttpResponse('BLAH')


def profile(request):
    #print(len(request.user.userskill_set.all()))

    # for user_skill in request.user.userskill_set.all():
    #     print(dir(user_skill))

    return render(request, 'brainex/results.html', {'user': request.user, 'skills': Skill.objects.all()})
#


def match(request):
    users = User.objects.all()
    user_list = {'users': []}
    for user in users:
        user_list['users'].append({'id': user.id, 'name': user.username})
    return render(request, 'brainex/home.html', user_list)