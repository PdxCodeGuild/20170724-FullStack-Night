# Django Quickstart



## Create a Project and App
- Create a site/project: `django-admin startproject <site/project name>`
- Move into the site's directory: `cd <site/project name>`
- Create an app: `python manage.py startapp <app-name>`
- Create a `urls.py` inside your app
- Add a route in your app's `urls.py` which points to the the view

```python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.<viewname>, name='<viewname>'),
]
```
- Add a route in your project's `urls.py` which points to the app's `url.py` using `include`

```python
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^<path>/', include('<appname>.urls'))
]
```


- Add your app (`appname.apps.AppnameConfig`) to the `INSTALLED_APPS` in `settings.py`

## Create Models

- Define your models (Python classes) in the app's `models.py`
- Stage your migrations: `python manage.py makemigrations <appname>`
- (optional) View the SQL commands that will occur during migrations: `python manage.py sqlmigrate <appname> <migration number>`. You can find the migration number and the code that'll be executed during the migration in `<appname>/migrations/<migration number>_initial.py`
- Perform migrations (synchronize your models with your database): `python manage.py migrate`

## Set Up Admin Interface

- Create an admin account `python manage.py createsuperuser`
- Enter your username, email address, and password
- Go to `localhost/admin` in your browser
- Make your app visible in the admin panel by registering our models with our app's `admin.py`


## Other Stuff

- Run the server: `python manage.py runserver`
- Access the shell `python manage.py shell`
