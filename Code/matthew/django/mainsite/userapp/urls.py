
from django.conf.urls import url
from . import views

app_name = 'userapp'
urlpatterns = [
    url('login/', views.config, name='config'),
    url('home/', views.addurl, name='addurl'),
    url(r'(?P<code>[a-zA-Z0-9]+)/', views.reroute, name='reroute')
]



