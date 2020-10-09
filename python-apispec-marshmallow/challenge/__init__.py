from datetime import datetime

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin

from flask import Flask, jsonify
from flask_cors import CORS

from marshmallow import Schema, fields


__version__ = '0.1.0'


app = Flask(__name__)
# Disable CORS
cors = CORS(app, resources={r'*': {'origins': '*'}})

# Fake data, let's assume they come from database.
USERS = [
    {'id': 1, 'email': 'bob@marley.com', 'firstname': 'Bob', 'lastname': 'Marley'},
    {'id': 2, 'email': 'jmjarre@dance.com', 'firstname': 'Jean-Michel', 'lastname': 'Jarre'},
    {'id': 3, 'email': 'me@fight.com', 'firstname': 'Conor', 'lastname': 'McGregor'},
]

BOOKS = [
    {'id': 1, 'name': 'L\'insoutenable légèreté de l\'être'},
    {'id': 2, 'name': 'La promesse de l\'aube'},
]

MOVIES = [
    {'id': 1, 'name': 'Fight Club', 'date': datetime(1999, 11, 10)},
    {'id': 2, 'name': 'American History X', 'date': datetime(1999, 3, 3)},
]


# Marshmallow schemas.
class UserSchema(Schema):
    id = fields.Integer()
    email = fields.String()
    firstname = fields.String()
    lastname = fields.String()


class BookSchema(Schema):
    id = fields.Integer()
    name = fields.String()


class MovieSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    date = fields.Date()


def add_data_wrapper(ToWrapSchema):
    """This function exists to avoid code duplication. It returns a marshmallow
    Schema with one field, "data", which is a nested field to the Schema
    provided as argument.

    Examples:

        >>> class MySchema(Schema):
        ...     name = fields.String()

        >>> items = [{"name": "xxx"}, {"name": "yyy"}]

        >>> MySchema().dump(items, many=True)
        [{"name": "xxx"}, {"name": "yyy"}]

        >>> add_data_wrapper(MySchema).dump({'data': items})
        {"data": [{"name": "xxx"}, {"name": "yyy"}]}
    """
    class DataSchema(Schema):
        data = fields.List(fields.Nested(ToWrapSchema))
    return DataSchema


WrappedBookSchema = add_data_wrapper(BookSchema)
WrappedMovieSchema = add_data_wrapper(MovieSchema)


@app.route('/')
def root():
    return jsonify({
        'message': 'Welcome to the API challenge. Documentation is available at /swagger.json.'
    })


@app.route('/users')
def users_list():
    """List users.
    ---
    get:
      description: List users.
      responses:
        200:
          content:
            application/json:
              schema: UserSchema
    """
    schema = UserSchema()
    resp = schema.dump(USERS, many=True)
    return jsonify(resp)


@app.route('/books')
def books_list():
    """List books.
    ---
    get:
      description: List books.
      responses:
        200:
          content:
            application/json:
              schema: WrappedBookSchema
    """
    schema = WrappedBookSchema()
    resp = schema.dump({'data': BOOKS})
    return jsonify(resp)


@app.route('/movies')
def movies_list():
    """List movies.
    ---
    get:
      description: List movies.
      responses:
        200:
          content:
            application/json:
              schema: WrappedMovieSchema
    """
    schema = WrappedMovieSchema()
    resp = schema.dump({'data': MOVIES})
    return jsonify(resp)


# Setup apispec to generate documentation
spec = APISpec(
    title='Swagger Petstore',
    version=__version__,
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)


# Register routes for documentation
with app.test_request_context():
    spec.path(view=users_list)
    spec.path(view=books_list)
    spec.path(view=movies_list)


# Endpoint consumed by swagger-ui
@app.route('/swagger.json')
def swagger():
    return jsonify(spec.to_dict())
