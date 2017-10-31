from django.conf.urls import url

from . import views

app_name = 'todoapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/', views.add, name='add'),
    url(r'^complete/', views.complete, name='complete')
    ]