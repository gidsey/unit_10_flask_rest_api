from flask import Blueprint, url_for

from flask_restful import Resource, Api, reqparse, inputs, fields, marshal, marshal_with, abort

import models

user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String
}


class UserList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'username',
            required=True,
            help='No username provided',
            location = ['form', 'json']
        )
        self.reqparse.add_argument(
            'email',
            required=True,
            help='No email provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'password',
            required=True,
            help='No password provided',
            location=['form', 'json']
        )
        super().__init__()

    def get(self):
        users = [marshal(user, user_fields) for user in models.User.select()]
        return {'users': users}


users_api = Blueprint('resources.users', __name__)
api = Api(users_api)

api.add_resource(
    UserList,
    '/users',
    endpoint='users'
)

