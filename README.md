# Flask API

An api built using [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/) and
[PeeWee](https://peewee.readthedocs.io/en/latest/index.html) ORM to interegate a Sqlite Database 
with Courses and Reviews models.

## Resources
URIs relative to http://127.0.0.1:5000/api/v1/

### Users 
Method    | Endpoint        |Data                   | Description              | Authentication | Rate Limited 
----------|-----------------|-----------------------|--------------------------|----------------|--------
|GET      | users           |                       | list all users           | No             |No           
|POST     | users           |username<br>email<br>password<br>verify_password | create user  | No |Yes

### Courses
Method    | Endpoint        |Data                   | Description              | Authentication | Rate Limited 
----------|-----------------|-----------------------|--------------------------|----------------|--------
|GET      | courses         |                       | list all courses        | No             |No           
|GET      | courses/id      |course_id              | course detail            | No             |No

### Reviews
Method    | Endpoint        |Data                   | Description              | Authentication | Rate Limited 
----------|-----------------|-----------------------|--------------------------|----------------|--------
|GET      |  reviews        |                       | list all reviews        | No             |No           
|GET      |  reviews/id     |review_id              | review detail            | No             |No




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