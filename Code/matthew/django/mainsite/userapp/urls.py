
from django.conf.urls import url
from . import views

app_name = 'userapp'
urlpatterns = [
    url('login/', views.login, name='login'),
]



