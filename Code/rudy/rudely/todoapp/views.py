


from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.shortcuts import render
from .models import TodoItem
from django.views.decorators.csrf import csrf_exempt


def index(request):
    todo_items = TodoItem.objects.filter(date_completed__isnull=True)  # .all() unpacks all the items in the TodoItems Class
    todo_completed = TodoItem.objects.filter(date_completed__isnull=False)
    context = {'todo_items': todo_items, 'todo_completed': todo_completed}  # a dictionary that keys the named items
    return render(request, 'todoapp/index.html', context) #returns request and the index.htm in the todoapp directory


def add(request):
    todo_text = request.POST['todo_text']       # gets the todo_text from the POST request on form in index.html
    #return HttpResponse('Hello')
    todo_item = TodoItem(todo_text=todo_text,
                         date_entered=timezone.now(), date_completed=None)
    todo_item.save()  #saves the todo_item to the database

    return HttpResponseRedirect(reverse('todoapp:index')) # redirects the user back to todoapp using the index view


def complete(request):
    todo_item_id = request.POST['todo_item_id']
    todo_item = TodoItem.objects.get(pk=todo_item_id)
    todo_item.completed =True
    todo_item.date_completed = timezone.now()
    todo_item.save()

    return HttpResponseRedirect(reverse('todoapp:index'))