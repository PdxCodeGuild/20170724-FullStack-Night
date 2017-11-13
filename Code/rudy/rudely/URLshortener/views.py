from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Shortener
import random, string


def index(request):
    original_url = Shortener.objects.all()
    code = Shortener.objects.all()
    context = {'original_url': original_url, 'code': code}
    return render(request, 'URLshortener/index.html', context)


def generate_code(n):
    r = ''
    for i in range(n):
        r += random.choice(string.number + string.letter)
    return r

def code_generator(request):
    url_text = request.POST['url_text']
    original_url = Shortener(original_url=url_text, code=None)
    return HttpResponse('Generator route is working!')
    #return HttpResponseRedirect(reverss('URLshortener:index'))


def code_converter(request, code):
    s = Shortener.objects.get(code=code)
    #return HttpResponse('Converter route is working!')
    return HttpResponseRedirect(s.original_url)
