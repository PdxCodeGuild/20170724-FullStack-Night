from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from .models import TodoAjaxItem
import json


def index(request):
    return render(request, 'todosajax/index.html', {})


def getitems(request):

    items = TodoAjaxItem.objects.all()
    data_dict = {'items': []}
    for item in items:
        data_dict['items'].append(item.todo_text)
    print(data_dict)
    return JsonResponse(data_dict)


def postitem(request):
    data = json.loads(request.body)
    item = TodoAjaxItem(todo_text=data['todo_text'], date_entered=timezone.now(), date_completed=None)
    item.save()
    return HttpResponse('OK')
