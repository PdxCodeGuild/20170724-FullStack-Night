from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from .models import TodoItem
from django.urls import reverse


def index(request):
    todo_items = TodoItem.objects.filter(completed=False)
    todo_completed = TodoItem.objects.filter(completed=True)
    context = {'todo_items': todo_items, 'todo_completed': todo_completed}
    return render(request, 'todoapp/index.html', context)


def add(request):
    todo_text = request.POST['todo_text']
    todo_item = TodoItem(todo_text=todo_text, date_entered=timezone.now(), date_completed=None, completed=False)
    todo_item.save()

    return HttpResponseRedirect(reverse('todoapp:index'))


def complete(request):
    todo_item_id = request.POST['todo_item_id']
    todo_item = TodoItem.objects.get(pk=todo_item_id)
    todo_item.completed = True
    todo_item.date_completed = timezone.now()
    todo_item.save()

    return HttpResponseRedirect(reverse('todoapp:index'))