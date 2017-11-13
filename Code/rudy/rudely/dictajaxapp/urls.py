from django.conf.urls import url
from . import views

app_name = 'dictajaxapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getdict', views.getdict, name='getdict'),
    url(r'^create', views.createdict, name='createdict'),
    url(r'^delete/(?P<delete_id>[0-9]+)/', views.deletedict, name='deletedict')
]
