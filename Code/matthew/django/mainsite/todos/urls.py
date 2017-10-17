from django.conf.urls import url

from . import views

app_name = 'todos'
urlpatterns = [
    url('^$', views.index, name='index'),
    url('add/$', views.add, name='add'),
    url('complete/$', views.complete, name='complete')
]
