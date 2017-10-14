from django.conf.urls import url
from . import views

app_name = 'urlshortnerapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'(?P<code_text>[a-zA-Z0-9]+)/', views.code, name='code')
]
