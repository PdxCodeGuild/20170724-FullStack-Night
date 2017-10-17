from django.conf.urls import url
from . import views

app_name = 'urlshortener'
urlpatterns = [
    url('config/', views.config, name='config'),
    url('addurl/', views.addurl, name='addurl'),
    url(r'(?P<code>[a-zA-Z0-9]+)/', views.reroute, name='reroute')
]
