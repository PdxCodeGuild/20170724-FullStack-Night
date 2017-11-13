from django.conf.urls import url
from . import views

app_name = 'dictionaryajax'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getwords/', views.getwords, name='getwords')
]