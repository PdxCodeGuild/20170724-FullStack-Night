# Django Quickstart

## Create a Project and App
- Create a site/project: `django-admin startproject <site/project name>`
- Run the server: `python manage.py runserver`
- Create an app: `python manage.py startapp <app-name>`
- Create a `urls.py` inside your app
- Link your project's `url.py` to the app's `url.py` using `include`
- Add your app to the `INSTALLED_APPS` in `settings.py`

## Create Models

- Define your models (Python classes) in the app's `models.py`
- Perform migrations (synchronize your models with your database: `python manage.py migrate`

## Set Up Admin Interface

- Create an admin account `python manage.py createsuperuser`
- Enter your username, email address, and password
- Go to `localhost/admin` in your browser
- Make your app visible in the admin panel by registering our models with our app's `admin.py`


