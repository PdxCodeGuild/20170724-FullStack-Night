from django.conf.urls import url

from . import views

app_name = 'URLshortener'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^generator/', views.code_generator, name='generator'),
    url(r'^(?P<code>[a-zA-Z0-9]+)/$', views.code_converter, name='code')
]