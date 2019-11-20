from flask import jsonify, Blueprint, abort

from flask_restful import Resource, Api, reqparse, inputs
from playhouse.flask_utils import get_object_or_404

import models


class CourseList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'title',
            required=True,
            help='No course title provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'url',
            required=True,
            help='No course URL provided.',
            location=['form', 'json'],
            type=inputs.url
        )
        super().__init__()

    def get(self):
        return jsonify({'courses': [{'title': 'Python Basics'}]})

    def post(self):
        args = self.reqparse.parse_args()
        models.Course.create(**args)
        return jsonify({'courses': [{'title': 'Python Basics'}]})


class Course(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'title',
            required=True,
            help='No course title provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'url',
            required=True,
            help='No course URL provided.',
            location=['form', 'json'],
            type=inputs.url
        )
        super().__init__()

    def get(self, id):
        return jsonify({'title': 'Python Basics'})

    def put(self, id):
        args = self.reqparse.parse_args()
        # course = models.Course.select().where(models.Course.id == id)

        try:
            course = models.Course.get(models.Course.id == id)
            print(course)
        except models.DoesNotExist:
            abort(404)

        print(course.title)

        return jsonify({'title': 'Python Basics'})

    def delete(self, id):
        return jsonify({'title': 'Python Basics'})


courses_api = Blueprint('resources.courses', __name__)
api = Api(courses_api)
api.add_resource(
    CourseList,
    '/api/v1/courses',
    endpoint='courses'
)

api.add_resource(
    Course,
    '/api/v1/courses/<int:id>',
    endpoint='course'
)
