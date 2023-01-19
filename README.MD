# INTRODUCTION


## Steps taken to complete the Wine-Shop
1. Create project, its apps and link it all to the main project.
2. Build our Models:
    * Order
    * OrderItem
    * Category
    * Country
    * Region 
    * Wine
3. Building a shopping cart
4. 

# Shopping Cart

To build the shopping cart we had use the Django Sessions Framework which allows us to store data for each visitor. The data will be stored on the server with the help of cookies to with the session ID.

We have used the session middleware to manage the sending and receiving of the cookies.

The Middleware which manages the sessions is the one bellow, and it is created automatically when we start a new project.
'django.contrib.sessions.middleware.SessionMiddleware'

We can access the current session by using the request.session

examples of session settings:

```
SESSION_COOKIE_AGE: The duration of session cookies in seconds. The default value is 1209600 (two weeks).
SESSION_COOKIE_DOMAIN: The domain used for session cookies. Set this to mydomain.com to enable cross-domain cookies or use None for a standard domain cookie.
SESSION_COOKIE_HTTPONLY: Whether to use HttpOnly flag on the session cookie. If this is set to True, client-side JavaScript will not be able to access the session cookie. The default value is True for increased security against user session hijacking.
SESSION_COOKIE_SECURE: A Boolean indicating that the cookie should only be sent if the connection is an HTTPS connection. The default value is False.
SESSION_EXPIRE_AT_BROWSER_CLOSE: A Boolean indicating that the session has to expire when the browser is closed. The default value is False.
SESSION_SAVE_EVERY_REQUEST: A Boolean that, if True, will save the session to the database on every request. The session expiration is also updated each time it's saved. The default value is False.
```

For more information on Sessions;
https://docs.djangoproject.com/en/4.0/ref/settings/#sessions.

## Storing shopping carts in sessions

To store the shooping cart in sessions we have created a structure to be serialized to json.

This structure has been created on the *cart.py*  file


# Custumers Orders

Once the costumer has checked out we have to register the order in the database 

We have created 2 Models, one for costumer information and a second one for the order items
### ModelInline

We have created 2 models one for the costumer information and a second one for items orders, we have then used the ModelInline class for the items order model in order to include it as an inline form inside the Orders admin form.

## Form
Once the Models have been created is now time to create the checkout form 

# Context processors

For now the message "Your cart is empty" is constantly displayed, we will now change it in order to show the number of items and the total amount.

As this information has to be displayed in all pages, we have to create a context processor to include the current cart in the request context.

## A context processor 
is a Python function that takes the request object as an argument and returns a dictionary that gets added to the request context. 
Context processors come in handy when we need to make something available globally to all templates.

### step1

Create context_processor.py file which will return our cart as a Dictionary

### step3
add it the file to our settings, 'context_processors': [... ]


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

When running the application on developing mode we have to remember to run the following code on terminal 
```
stripe listen --forward-to localhost:8000/payment/webhook/
```

## IMPORTANT- SECURITY

We have build a webhook endpoint which receives a json payload with the event detail, we then check the details to identify when a checkout session has been completed.
WE MUST ALWAYS CHECK THE *Stripe-Signature* ON IN EACH EVENT SENT TO OUR ENDPOINT TO AVOID THIRD PARTY ATTACKS.
The Stripe SDK provides a method to verify signatures.

The end point is created on the file webhooks.py, where we will check the information sent by Stripe and if everything is correct we will then update our Order models to save the field paid as True.

## Testing webhook notifications with Stripe CLI 

https://stripe.com/docs/stripe-cli#install.


# Coupon System
We have created a new app on our Django project to allow our shop to use discount coupons.

For that a new Model has been created a model which allow us to generate discount coupons to be used n number of times and to be applied to the whole shopping cart, the coupons should have an expering date. 




# Deploying 

## Dockerfile
Created Dockerfile:
  where we specifie which version of Python alpine version (alpine is a lightweight version for python ideal for docker) we are using and install all the dependencies of our application

## Docker-Compose
Created docker-composed to run the development server:




