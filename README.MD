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

