# Shopping Cart

To build the shopping cart we will be using the Django Sessions Framework which will allow us to store data for each visitor. The data will be stored on the server with the help of cookies to with the session ID.

we will be using the session middleware to manages the sending and receiving of the cookies.

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

To store the shooping cart in sessions we will create a structure which will then be serialized to json