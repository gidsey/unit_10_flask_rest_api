# Flask API

An api built using [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/) and
[PeeWee](https://peewee.readthedocs.io/en/latest/index.html) ORM to interegate a Sqlite Database 
with Courses and Reviews models.

## Resources
URIs relative to http://127.0.0.1:5000/api/v1/

### Users 
Method    | Endpoint        |Data                   | Description              | Auth Req? | Rate Limited? 
----------|-----------------|-----------------------|--------------------------|----------------|--------
|GET      | users           |                       | list all users           | ✖             | ✖           
|POST     | users           |username<br>email<br>password<br>verify_password  | create user  | ✖ |✔

### Courses
Method    | Endpoint        |Data                   | Description              | Auth Req? | Rate Limited? 
----------|-----------------|-----------------------|--------------------------|----------------|--------
|GET      | courses         |                       | list all courses        | ✖              |✖           
|POST     | courses         |title<br>url           | create course           | ✔             |✔
|GET      | courses/id      |             | course detail           | ✖              |✖
|PUT      | courses/id      |title<br>url           | edit course             | ✔             |✔

### Reviews
Method    | Endpoint        |Data                   | Description              | Auth Req? | Rate Limited? 
----------|-----------------|-----------------------|--------------------------|----------------|--------
|GET      |  reviews        |                       | list all reviews        | ✖             |✖           
|GET      |  reviews/id     |review_id              | review detail            | ✖             |✖
|POST| reviews|course<br>rating(1-5)<br>comment(optional)| create review as signed-in user|✔|✔
|PUT| reviews/id|course<br>rating(1-5)<br>comment(optional)| edit review as signed-in user|✔|✔
|DELETE| reviews/id|| immediately delete selcetd review |✔|✔


### Notes

Using Postman, submit a POST request to the /courses endpoint with new course information plus basic auth credentails 
to replicate logging he user in.

Once loggedin, go to /users/token to generate a token for that user. Set Auth to none and add token to the Authorization 
key in Postman to use as autentication method. 

## Features

* Password hashing with [Argon2](https://github.com/p-h-c/phc-winner-argon2)
* Token authentication with [itsdangerous](https://pythonhosted.org/itsdangerous/)
* Rate limiting with [FlaskLimiter](https://flask-limiter.readthedocs.io/en/stable/)


## Running Locally

```bash
git clone https://github.com/gidsey/unit_10_flask_rest_api.git
```

```bash
pip install -r requirements.txt
```

```bash
 python app.py
```