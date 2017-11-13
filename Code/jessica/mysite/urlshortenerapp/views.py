from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import Shortener
import string
import random


# Create your views here.


def index(request):
    latest_urls = Shortener.objects.all()
    context = {'shorteners': latest_urls}
    return render(request, 'urlshortenerapp/index.html', context)


def code(request, code_text):
    url_code = get_object_or_404(Shortener, code_text=code_text)
    return HttpResponseRedirect(url_code.url_text)


def code_generator():
    r = ''
    for i in range(5):
        r += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    return r

def add(request):
    url = request.POST['url']
    url_text = Shortener(url_text=url, code_text=code_generator())
    url_text.save()
    return HttpResponseRedirect(reverse('urlshortenerapp:index'))

