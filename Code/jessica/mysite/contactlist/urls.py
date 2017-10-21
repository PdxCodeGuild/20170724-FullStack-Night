from django.conf.urls import url
from . import views

app_name = 'contactlist'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<name_id>[0-9]+)', views.detail, name='detail'),
    url(r'^add/', views.add, name='add'),
    url(r'^sms/', views.sms, name='sms')
]
