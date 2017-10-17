from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import UrlReroute

import random


def generate_code(n):
    r = ''
    for i in range(n):
        r += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    return r


def config(request):
    reroutes = UrlReroute.objects.all()
    context = {'reroutes': reroutes}
    return render(request, 'urlshortener/config.html', context)


def addurl(request):
    url = request.POST['url']
    code = generate_code(6)
    urr = UrlReroute(code=code, url=url)
    urr.save()
    return HttpResponseRedirect(reverse('urlshortener:config'))


def reroute(request, code):
    rr = get_object_or_404(UrlReroute, code=code)
    return HttpResponseRedirect(rr.url)
