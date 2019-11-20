from flask import jsonify, Blueprint, abort

from flask_restful import Resource, Api, reqparse, inputs

import models


class ReviewList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'course',
            required=True,
            help="No course ID provided",
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'rating',
            required=True,
            help="No course rating provided",
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'comment',
            required=False,
            location=['form', 'json']
        )

    def get(self):
        return jsonify({'reviews': [{'course': 1, 'rating': 5}]})

    def post(self):
        args = self.reqparse.parse_args()

        models.Review.create(**args)
        # for value in args.values():
        #     print(value)
        #     # print(value)
        #
        # try:
        #     course = models.Course.get(models.Course.id == id)
        # except models.DoesNotExist:
        #     abort(404)
        # else:
        #     pass

        return jsonify({'reviews': [{'course': 1, 'rating': 5}]})


class Review(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'rating',
            required=True,
            help="No course rating provided",
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'comment',
            required=False,
            location=['form', 'json']
        )

    def get(self, id):
        return jsonify({'course': 1, 'rating': 5})

    def put(self, id):
        args = self.reqparse.parse_args()
        try:
            review = models.Review.get(models.Review.id == id)
        except models.DoesNotExist:
            abort(404)
        print(review)
        print(review.comment)
        review.update(**args).execute()
        return jsonify({'course': 1, 'rating': 5})

    def delete(self, id):
        return jsonify({'course': 1, 'rating': 5})


reviews_api = Blueprint('resources.reviews', __name__)

api = Api(reviews_api)
api.add_resource(
    ReviewList,
    '/reviews',
    endpoint='reviews'
)
api.add_resource(
    Review,
    '/reviews/<int:id>',
    endpoint='review'
)


