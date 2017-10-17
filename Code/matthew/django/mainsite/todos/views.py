from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import TodoItem


def index(request):
    todo_items = TodoItem.objects.filter(date_completed__isnull=True)
    todo_completed = TodoItem.objects.filter(date_completed__isnull=False)
    context = {'todo_items': todo_items, 'todo_completed': todo_completed}
    return render(request, 'todos/index.html', context)




def add(request):
    todo_text = request.POST['todo_text']
    todo_item = TodoItem(todo_text=todo_text, date_entered=timezone.now(), date_completed=None)
    todo_item.save()

    return HttpResponseRedirect(reverse('todos:index'))


def complete(request):
    todo_item_id = request.POST['todo_item_id']
    todo_item = TodoItem.objects.get(pk=todo_item_id)
    todo_item.date_completed = timezone.now()
    todo_item.save()
    return HttpResponseRedirect(reverse('todos:index'))

