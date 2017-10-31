from django.conf.urls import url
from . import views

app_name = 'ContactList'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^(?P<contact_id>[0-9]+)/$', views.detail, name='detail'),
]
