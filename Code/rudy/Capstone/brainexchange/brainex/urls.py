from django.conf.urls import url
from . import views

app_name = 'brainex'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login_user, name='login'),
    url(r'^registration/', views.registration, name='registration'),
    url(r'^createuser/', views.create_user, name='createuser'),
    url(r'^profile/', views.profile, name='profile')
]