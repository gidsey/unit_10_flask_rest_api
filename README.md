# Flask API

An api built using [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/) and
[PeeWee](https://peewee.readthedocs.io/en/latest/index.html) ORM to interegate a Sqlite Database 
with Courses and Reviews models.

## Resources
URIs relative to http://127.0.0.1:5000/

### Anonymous users
Method    | Endpoint | Data                    | Description 
---------|------------|----------------------|-------------
|GET      | api/v1/courses    |              | returns list of all courses
|GET      | api/v1/courses |course_id      | returns course detail


### Auhenticated users
Method    | Endpoint    |Data                   | Description 
---------|---------------|-------------------|-------------
|POST     | api/v1/courses |title (required) <br>url (required)| creates a new couusre



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