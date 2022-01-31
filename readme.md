##### Introduction

***The goal of this project is to implement a ecommerce REST api allowing for basic CRUD functionality for orders and product endpoints. Additionally, there is functionality for running periodic tasks in the background using celery and message broker as redis***


##### Main features

**CRUD of Orders and Products with Django DRF**

**Basic token authentication and authorization**

**Custom permissions with filtering, ordering specific fields and pagination**

**Managaement command for saving a dataframe in Django model using Pandas**

**Running background tasks using celery and redis backend**

**Using a production database similar to mysql for robust implementations**

**Separation of dev and production settings for deployments and configuring env variables**


##### Usage


Existing virtualenv


If your project is already in an existing python3 virtualenv first install django by running

`$ pip install django`


And then run the django-admin.py command to start the new project:

`$ django-admin startproject <your_project_name>`


After that just install the local dependencies, run migrations, and start the server.


###### Getting Started


First clone the repository from Github and switch to the new directory:

```
$ git clone git@github.com/USERNAME/{{ project_name }}.git
$ cd {{ project_name }}
```

Activate the virtualenv for your project


Install project dependencies:

```
$ pip install -r requirements.txt
```

Then simply apply the migrations:

```
$ python manage.py migrate
```

You can now run the development server:

```
$ python manage.py runserver
```

Alternately create a superuser or admin using:

```
$ python manage.py createsuperuser
```

##### REST API documentation


> You can register new users here:

http://127.0.0.1:8000/auth/users/



> You can create your access and refresh tokens for logging in:

http://127.0.0.1:8000/auth/jwt/create



> You can access your own profile here, for this you need to install a chrome extension like MODHEADER to authenticate yourself by passing request header for authorization:

http://127.0.0.1:8000/auth/users/me/



> After registering a new user, you can access the customers endpoint here:

http://127.0.0.1:8000/store/customers/



> You can access the products endpoint to retreive your own products:

http://127.0.0.1:8000/store/products/



> You can access the orders endpoint to retreive your own orders:

http://127.0.0.1:8000/store/orders/


***Alternately, you can access the products and orders endpoint to perform basic CRUD operations as admin to understand how the API works***



**Run the management command in store/management/commands/add_data.py to save data from excel file into Django model using pandas**

```
manage add_data.py
```


**Running background tasks using celery**


You can setup and configure celery to run tasks in background and use message broker like redis on another port


*Note: You need to install and configure docker and add it to the path before starting a redis server*


Using a separate terminal launch a redis instance using this docker command:

```
$ docker run -d -p 6379:6379 redis
```

Now on another terminal launch celery worker that can listen for your tasks and execute them in the background


A basic example can be like this:

```
$ celery -A <name_of_your_app> worker --loglevel=info
```

You can use celery beat to listen for peroidic tasks using cron in the background on a separate terminal:

```
$ celery -A <name_of_your_app> beat
```

*Note: You have to correctly import celery with respect to your settings module for celery to discover and execute the tasks*


##### Deployment settings:


use dev.py for local development and testing


and prod.py for production


> For production settings set from your environment variables .env file:

````
SECRET_KEY = config('SECRET_KEY')
````

```
DEBUG = False
```

Configure database settings for your database of choice for example:

```
DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.mysql",
                "HOST" : config('DB_HOST', default='localhost'),
                "NAME": config('DB_NAME'),
                "USER": config('DB_USER'),
                "PASSWORD": config('DB_PASSWORD'),
                "PORT": "config('DB_PORT)
            }
 }
```


**Please use the .env-sample as a reference**


For production use [gunicorn](https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/gunicorn/):

```
$ gunicorn your_app_name.wsgi
```

##### References


***You can reference the [django documentation](https://docs.djangoproject.com/en/4.0/) here:***



***Or look for solutions to a particular problem you have encountered in this project [here](https://stackoverflow.com/):***



***For more information regarding an issue, please submit a pull request***
