from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^login/', auth_views.login, name='login'),
    url(r'^logout/', auth_views.logout, name='logout'),
    url(r'^registration-core/', include('core.urls')),
    url(r'^brainex/', include('brainex.urls')),
    url(r'^admin/', admin.site.urls)
]
