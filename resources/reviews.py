from flask import jsonify, Blueprint

from flask_restful import Resource, Api, reqparse, inputs,  fields, marshal, marshal_with, abort

import models

review_fields = {
    'id': fields.Integer,
    'course_id': fields.Integer,
    'rating': fields.String,
    'comment': fields.String
}


def review_or_404(review_id):
    try:
        review = models.Review.get(models.Review.id == review_id)
    except models.Review.DoesNotExist:
        abort(404, message='Review {} does not exist'.format(review_id))
    else:
        return review


class ReviewList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'course',
            type=inputs.positive,
            required=True,
            help="No course ID provided",
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'rating',
            type=inputs.int_range(1,5),
            required=True,
            help="No course rating provided",
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'comment',
            required=False,
            nullable=True,
            location=['form', 'json'],
            default=''
        )
        super().__init__()

    def get(self):
        reviews = [marshal(review, review_fields) for review in models.Review.select()]
        # print(reviews)
        return {'reviews': reviews}

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
        super().__init__()

    @marshal_with(review_fields)
    def get(self, id):
        return review_or_404(id)

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


