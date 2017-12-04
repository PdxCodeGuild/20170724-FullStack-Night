
from django.conf.urls import url

from . import views

app_name = 'todosajax2'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'getdata/', views.getdata, name='getdata'),
    url(r'setdata/', views.setdata, name='setdata')
]


