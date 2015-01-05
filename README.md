# Another Heroku Django Starter Template

A project heavily inspired by https://github.com/heroku/heroku-django-template & https://github.com/rdegges/django-skel

## Features

- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's statc file serving functionality via WhiteNoise
- Enhancements to Django's database functionality via django-postgrespool and dj-database-url
- Separate settings and requirements files for development and production environments
- Development debug toolbar installed for local dev environment 
- A few more basic starter heroku add-ons added for performance tracking, caching and email

## How to Use

To use this project, follow these steps:

1. Create your working environment.
2. Install Django (`$ pip install django`)
3. Create a new project using this template

## Creating Your Project

Using this template to create a new Django app is easy::

    $ django-admin.py startproject --template=https://github.com/abhimskywalker/heroku-django-template/archive/master.zip --name=Procfile helloworld

You can replace ``helloworld`` with your desired project name.

## Deployment to Heroku 

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"
    $
    $ heroku create
    $ git push heroku master
    $
    $ # replace 'helloworld' with your django project name that you used above to initialize it
    $ heroku config:set DJANGO_SETTINGS_MODULE='helloworld.settings.prod'
    $ heroku config:set SECRET_KEY=`openssl rand -base64 32`
    $
    $ # https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/#python-options
    $ heroku config:set PYTHONHASHSEED=random
    $
    $ heroku run python manage.py syncdb

## Adding the basic addons to Heroku app

    $ heroku addons:add newrelic:stark
    $ heroku config:set NEW_RELIC_APP_NAME='helloworld Web Site (Production)'
    $ heroku addons:add memcachier
    $ heroku addons:add papertrail
    $ heroku addons:add mandrill

## Now rejoice on setting up the basic django app on heroku, and start developing on local

    $ # Personal habit to make manage.py executable. 
    $ # instead of `python manage.py runserver` now you can write `./manage.py runserver`
    $ chmod +x manage.py
    
    $ # To start local server with debug toolbar just run: 
    $ ./manage.py runserver


## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [django-postgrespool](https://warehouse.python.org/project/django-postgrespool/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
- [newrelic](https://warehouse.python.org/project/newrelic/)
- [django-heroku-memcacheify](https://warehouse.python.org/project/django-heroku-memcacheify/)
- [djrill](https://warehouse.python.org/project/djrill/)

## TODO:
- Add functionality to facilitate workers
