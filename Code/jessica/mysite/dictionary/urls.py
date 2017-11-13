from django.conf.urls import url
from . import views

app_name = 'dictionary'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<word_id>[0-9]+)/', views.detail, name='detail'),
    url(r'^add/', views.add, name='add')

]