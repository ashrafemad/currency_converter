# currency_converter
Convert Currencies API

# Prerequisites
* make sure to have python3.6 or above and created a virtual environment for this project

* install [postgres database](https://www.postgresql.org/download/)

* follow the [instructions here to install celery](https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html#first-steps) with RabbitMQ


# Steps to run

1- clone the master branch

2- make sure to place `.env` file in the root directory [there is an env.example file](example.env) to be used as reference

3- activate your venv

4- run `pip install -r requirements.txt` to install dependencies

5- run `python manage.py migrate`

6- run `python manage.py createsuperuser` to create a superuser

7- start celery and celery beat using these commands `celery -A currency_converter worker -l INFO` then `celery -A currency_converter beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler`

8- run `python manage.py runserver` to start the server


# Using the Application

* Initial currencies to be created (EUR - USD - EGP)

* Conversion rates can be periodically updated by navigating to admin `/admin/django_celery_beat/periodictask/` and create a new task with your preferred options so it can be scheduled 

* you can find API docs in `/api/docs/`

