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


