from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json


def index(request):
    return render(request, 'ajaxdemo/index.html', {})


def postdata(request):
    received_json_data = json.loads(request.body)
    print(received_json_data)
    return HttpResponse('OK')


def getdata(request):
    data = {'foo': 'bar', 'hello': 'world'}
    return JsonResponse(data)
