from .common import *

DEBUG = True

SECRET_KEY = 'django-insecure-24feon*)_o_vjuk9ie=7g*++aa7w@xnv=z&=wwfmh3zmw5f@@q'

DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.mysql",
                "HOST" : config('DB_HOST', default='localhost'),
                "NAME": config('DB_NAME'),
                "USER": config('DB_USER'),
                "PASSWORD": config('DB_PASSWORD'),
                "PORT": "3306",
            }
 
 }