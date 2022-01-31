from time import sleep
from celery import shared_task
from django.core.management import call_command 

@shared_task
def add_data():
    call_command("add_data", )