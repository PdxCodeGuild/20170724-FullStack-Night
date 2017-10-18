
from django.conf.urls import url
from . import views

app_name = 'ajaxdemo'
urlpatterns = [
    url('^$', views.index, name='index'),
    url('postdata/', views.postdata, name='postdata'),
    url('getdata/', views.getdata, name='getdata')
]
