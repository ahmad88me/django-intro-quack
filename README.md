# django-intro-quack

## Setup
1. [pip](https://pip.pypa.io/en/stable/installing/)
2. Install Django `pip install Django` [more](https://www.djangoproject.com/download/)
3. Create a project names quack `django-admin startproject quack`
4. Test the landing page `python manage.py runserver`
5. add 'models.py' and 'views.py' or use 'startapp' [more](https://docs.djangoproject.com/en/2.0/intro/tutorial01/)
6. sync the db: `python manage.py makemigrations quack` `python manage.py migrate` 
7. create a superuser `python manage.py createsuperuser --username=aalobaid --email=aalobaid@fi.upm.es`
8. download [bootstrap template](https://startbootstrap.com/template-overviews/bare/).


## Templates setup
1. add 'quack' to `INSTALLED_APPS` in 'settings.py'
2. add `os.path.join(BASE_DIR, 'quack/templates')` to `DIRS` under `TEMPLATES` in the `settings.py` file.

## Important topics
* [template language](https://docs.djangoproject.com/en/1.7/topics/templates/)
