# Asynchronous Tasks

## Workers, Message Queues, and Message Brokers

While your web server processes requests and returns responses, you need a second task-based server, 
named worker, to process the asynchronous tasks. One or multiple workers can be running and executing 
tasks in the background. These workers can access the database, process files, send e-mails, etc. 
Workers can even queue future tasks. All while keeping the main web server free to process HTTP requests.

To tell the workers what tasks to execute we need to send messages. We communicate with brokers by 
adding messages to a message queue, which is basically a first in, first out (FIFO) data structure. 

## RabbitMQ AND Celery

On our application we will be using RabbitMQ as a Message broker and the Celery to manage our workers.

*RabbitMW* is a message broker that implements the Advanced Message Queuing Protocol (AMQP), which standardizes messaging using Producers, broker and Consumers, it helps to increase loose coupling and scalability.
The RabbitMQ receives a message from the producer(application), it will then direct this message to the relevant queue so it can wait it's turn to be processed by the worker (which in our case will be managed by Celery).
RabbitMQ has 5 different types of exchanges (ways), to move the message to the relevant queue:
    - fanout
    - direct
    - topic
    - header
    - default


*Celery*, not only allow you to create asynchronous tasks easily and let them be executed by 
workers as soon as possible, but you can also schedule them to run at a specific time. 
https://docs.celeryq.dev/en/stable/index.html.


###  - Setting up *RabbitMQ*

```
docker pull rabbitm
```

```
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.9-management
```

we can then access our RabbitMQ dashboard on http://127.0.0.1:15672/ 


###   - Setting up Celery

create a new file on the root folder called celery.py and add the following code:

```
import os
from celery import Celery
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wine_shop.settings')
app = Celery('wine_shop')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
```

We have then to add the following code to the __init--.py found on our project folder (wine_shop)
```
# import celery
from .celery import app as celery_app
__all__ = ['celery_app']
```

With all this done we can now start using Celery on our program

