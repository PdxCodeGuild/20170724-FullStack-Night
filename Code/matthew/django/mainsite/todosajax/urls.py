from django.conf.urls import url

from . import views

app_name = 'todosajax'
urlpatterns = [
    url('^$', views.index, name='index'),
    url('getitems/', views.getitems, name='getitems'),
    url('postitem/', views.postitem, name='postitem')
]
