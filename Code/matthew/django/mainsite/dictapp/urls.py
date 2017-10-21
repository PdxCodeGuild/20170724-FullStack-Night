
from django.conf.urls import url
from . import views

app_name = 'dictapp'
urlpatterns = [
    url('^$', views.index, name='index'),
    url('detail/(?P<entry_id>[0-9]+)', views.detail, name='detail')
]
