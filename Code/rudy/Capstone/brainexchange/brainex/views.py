from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User


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



def registration(request):
    return render(request, 'brainex/registration.html', {})


def create_user(request):
    new_username = request.POST['new_username']
    new_password = request.POST['new_password']
    new_first = request.POST['new_first']
    new_last = request.POST['new_last']
    new_email = request.POST['new_email']
    new_user = User.objects.create_user(username=new_username,
                                    password=new_password,
                                    email=new_email,
                                    first_name=new_first,
                                    last_name=new_last,
                                    )
    return HttpResponseRedirect(reverse('brainex:profile'))


def profile(request):
    username = request.user.username
    print(username)
    return render(request, 'brainex/results.html', {'username': username})


def match(request):
    pass