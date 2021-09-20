## Django y Celery & RabbitMQ (asincronía en Python)
-------------------------------------------------------------------
## Crear entorno virtual
virtualenv entorno_virtual -p python3

## Activar entorno virtual
source entorno_virtual/bin/activate

## Desativar entorno virtual
deactivate

## install requirements
$ pip install -r requirements.txt 

## crear proyecto
$ django-admin startproject app_celery

## cambiar carpeta app_celery a config
configurar ficheros en config

cd app_celery
$ celery/python3 manage.py runserver

## instalar rabbitmq
$ sudo apt-get install rabbitmq-server
$ sudo systemctl enable rabbitmq-server
$ sudo systemctl start rabbitmq-server

# instalar rabbitmq con docker
$ docker run -d -p 5672:5672 rabbitmq
http://localhost:5672/

$ docker container ls

# celery results
seguimiento en shell tasks ejecutadas
$ pip install django-celery-results

# docs celery
https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html

app_celery/ $ celery -A app.tasks worker --loglevel=INFO

# en el shell de django
$ python3 manage.py shell
>>> from app.tasks import add1, rest1, add2, rest2
>>> result=rest1.delay(3,1)
>>> result.ready() => true
>>> result.get(timeout=1) => 2




