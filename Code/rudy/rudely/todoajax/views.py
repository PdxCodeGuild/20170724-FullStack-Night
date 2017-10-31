from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
import json
from django.utils import timezone
from django.shortcuts import render
from .models import TodoajaxItem
from django.views.decorators.csrf import csrf_exempt


def index(request):
    todo_items = TodoajaxItem.objects.filter(date_completed__isnull=True)  # .all() unpacks all the items in the TodoItems Class
    todo_completed = TodoajaxItem.objects.filter(date_completed__isnull=False)
    context = {'todo_items': todo_items, 'todo_completed': todo_completed}  # a dictionary that keys the named items
    return render(request, 'todoajax/index.html', context) #returns request and the index.htm in the todoapp directory


def getdata(request):
    todo_items = TodoajaxItem.objects.all()
    data = {'todo_items': []}
    for todo_item in todo_items:
        data['todo_items'].append(todo_item.todo_text)
    return JsonResponse(data)


def setdata(request):
    data = json.loads(request.body)
    todo_text = data['todo_text']
    todo_item = TodoajaxItem(todo_text=todo_text, date_entered=timezone.now(), date_completed=None, completed=False)
    todo_item.save()
    return HttpResponse('setdata is working')

