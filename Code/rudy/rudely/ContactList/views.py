from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import Contact


def index(request):
    contact_items = Contact.objects.all()
    context = {'contact_items': contact_items}
    return render(request, 'ContactList/index.html', context)


def add(request):
    new_name = request.POST['new_name']
    new_color = request.POST['new_color']
    new_fruit = request.POST['new_fruit']
    new_contact = Contact(contact_name=new_name, contact_color=new_color, contact_fruit=new_fruit)
    new_contact.save()
    return HttpResponseRedirect(reverse('ContactList:index'))


def detail(request, contact_id):
    contact_item = get_object_or_404(Contact, pk=contact_id)
    return render(request, 'ContactList/detail.html', {'contact_item': contact_item})