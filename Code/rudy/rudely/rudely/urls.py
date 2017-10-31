from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^shortener/', include('URLshortener.urls')),
    url(r'^todoapp/', include('todoapp.urls')),
    url(r'^contact-list/', include('ContactList.urls')),
    url(r'^dictajax/', include('dictajaxapp.urls')),
    url(r'^todoajax/', include('todoajax.urls'))
]
