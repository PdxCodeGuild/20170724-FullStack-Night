from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import DictEntry


def index(request):
    entries = DictEntry.objects.order_by('word')
    context = {'entries': entries}
    return render(request, 'dictapp/index.html', context)


def add(request):
    return HttpResponse('add')


def detail(request, entry_id):
    entry = DictEntry.objects.get(pk=entry_id)
    context = {'entry': entry}
    return render(request, 'dictapp/detail.html', context)

