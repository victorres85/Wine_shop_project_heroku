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


# PAYMENT PROCESS WITH STRIPE

Our payment process will be used with stripe for that we have pip installed the stripe packet we have also opened an account on stripe where we are currently working on developing mode

To process the payment 3 views will be created: 
  - payment_process -> which will create a Stripe checkout session and redirects the lient to the Stripe-hosted payment form.
  - payment_completed -> which displays a message confirming the payment
  - payment_canceled -> which displays a message for canceled payments


On our settings we have added the keys colected from our stripe account, this is what will link our application to stripe. If the payment is sucessful stripe will redirect the user to the payment_completed.html otherwise will redirect the custumer to payment_canceled.html.

# Webhook
 
Stripe can push real-time events to our application by using webhooks. Which is an event driven API and not the request driven API we are used to. 

Stripe can send a HTTP request to a URL of our application to notify successful payments in real-time. These events will be notified asynchronously, when the event occurs.

We have builded a webhook endpoint to receive Stripe events. The webhook consists of a view that receives a JSON payload with the event information to process it. We use the event information to mark orders as paid when the checkout session is successfully completed.

https://dashboard.stripe.com/test/webhooks
On the website above we can see a schema of how Stripe notifies our our integration asynchronously.
We will be notified whenever an event happens. We can check all the types of events that Stripe sends at https://stripe.com/docs/api/events/types

By clicking on TEST on the stripe webhooks page we can find the steps to setup our local enviroment to listen to Stripe Webhooks and we can also find an example in python on how to build the  webhook on our application.

When running the application on developing mode we have to remember to run the following code on terminal stripe listen --forward-to localhost:8000/payment/webhook/

