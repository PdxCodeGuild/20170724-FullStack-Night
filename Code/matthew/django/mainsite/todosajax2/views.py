from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
import json

from .models import TodoItemAjax2

# Create your views here.

def index(request):
    return render(request, 'todosajax2/index.html', {})

def getdata(request):
    todo_items = TodoItemAjax2.objects.all()
    data = {'todo_items':[]}
    for todo_item in todo_items:
        data_item = {}
        data_item['id'] = todo_item.id
        data_item['text'] = todo_item.text
        data_item['completed'] = todo_item.completed
        data['todo_items'].append(data_item)
    return JsonResponse(data)

def setdata(request):
    data = json.loads(request.body)
    todo_text = data['todo_text']
    todo_item = TodoItemAjax2(text=todo_text, date_entered=timezone.now(), date_completed=None, completed=False)
    todo_item.save()

    return HttpResponse('OK')

