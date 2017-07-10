[![N|Solid](http://securityinside.info/wp-content/uploads/logo.png)](http://securityinside.info)

# Flask-api-template

[SecurityInside] template to get ready your own api in minutes using python and flask.

### Installation

flask-api-template is a [Python] 2.7 script.

### Execution

Development mode:
```sh
$ python flask_api.py
```

Production mode:
[Flask deployment options]

### Instructions for use
The following headers are common to all API services.
 - Authorization (mandatory):
   - Basic auth for /login service ("Basic base64(user:pass)")
   - Obtained JWT for all other services ("Bearer jwt_token")

The following response codes can be returned by any of the API services.

 - 200 - OK
 - 401 - UNAUTHORIZED
 - 403 - FORBIDDEN
 - 406 - NOT ACCEPTABLE
 - 412 - PRECONDITION_FAILED
 - 503 - SERVICE_UNAVAILABLE

```
For use examples, you have a postman file inside the repository with all the current methods.
```

[//]: # (Links section)

[SecurityInside]: <http://securityinside.info>
[Python]: <https://www.python.org/>
[Flask deployment options]: <http://flask.pocoo.org/docs/0.12/deploying/>
