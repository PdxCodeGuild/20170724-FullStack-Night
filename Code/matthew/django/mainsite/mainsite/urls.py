"""mainsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url('^admin/', admin.site.urls),
    url('^$', admin.site.urls),
    url('^dictapp/', include('dictapp.urls')),
    url('^ajaxdemo/', include('ajaxdemo.urls')),
    url(r'^polls/', include('polls.urls')),
    url('^todos/', include('todos.urls')),
    url('^todosajax/', include('todosajax.urls')),
    url(r'^urlshortener/', include('urlshortener.urls')),
    url(r'^todosajax2/', include('todosajax2.urls')),
    url(r'^user/', include('userapp.urls'))
]
