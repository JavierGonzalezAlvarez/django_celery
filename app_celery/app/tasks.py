# The @shared_task decorator lets you create tasks without
#   having any concrete app instance:

#from .views import sendEmail
import time
from celery import shared_task

from django.http import HttpResponse
from django.core.mail import EmailMessage

from celery import Celery

from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)

# instanciamos Celery
app = Celery('tasks', backend='rpc://', broker='pyamqp://')


@app.task
def add1(x, y):
    return x + y


@app.task
def rest1(x, y):
    return x - y


@shared_task
def add2(x, y):
    return x + y


@shared_task
def rest2(x, y):
    return x - y


@shared_task
def sendEmailTask(subject, message, sender):
    subject = subject
    message = message
    sender = sender
    email_message = EmailMessage(
        subject=subject,
        body=message,
        to=[sender],
    )
    email_message.send()
    html = "<html><body>Gracias por tu email</body></html>"
    return HttpResponse(html)


@shared_task
def mensaje(segundos):
    html = "<html><body>Gracias por tu email</body></html>"
    time.sleep(segundos)
    return HttpResponse(html)
