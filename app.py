from flask import Flask, request, jsonify, abort
from models import db_drop_and_create_all, setup_db, Movie, Actor
from flask_cors import CORS
import json
from env_file import request_uri
from auth import AuthError, requires_auth


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    '''
    @TODO uncomment the following line to initialize the datbase
    !! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
    !! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
    '''
    # db_drop_and_create_all()

    """
    Create a movie. title and release_date required.
    Returns the created movie as a list with one dictionary
    """
    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movie(payload):
        try:
            body = request.get_json()
            title = body.get('title', '')
            release_date = body.get('release_date', '')

            if len(title) == 0 or len(release_date) == 0:
                abort(400)

            movie = Movie(title=title, release_date=release_date)
            movie.insert()

            data = {
                'success': True,
                'movie': [movie.format_short()]
            }

            return jsonify(data)

        except Exception:
            abort(400)

    # format all movies and return the list
    def formatted_movies():
        # get all movies
        all_movies = Movie.query.order_by(Movie.id).all()
        formatted_movies = [
            movie.format() for movie in all_movies]
        return formatted_movies

    """
    Get the list of all movies
    """
    @app.route('/movies')
    @requires_auth('get:movies')
    def get_movies(payload):

        """
        This endpoint returns a list of all movies
        """
        try:
            data = {
                'success': True,
                'movies': formatted_movies()
            }

            # send data in json format
            return jsonify(data)

        except Exception:
            abort(404)

    """
    Update a movie. title or release_date required.
    Returns the updated movie as a list with one dictionary
    """
    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movie(payload, movie_id):
        try:
            # get the movie id from the url
            movie_id = int(movie_id)

            # fetch the movie with the id
            movie = Movie.query.filter(
                Movie.id == movie_id).one_or_none()

            # if no movie exists with that id, abort
            if movie is None:
                abort(400)

            # fetch the request body
            body = request.get_json()
            title = body.get('title', '')
            release_date = body.get('release_date', '')

            # if title and release_date both are empty, abort
            if len(title) == 0 and len(release_date) == 0:
                abort(400)

            # if title is available update it
            if len(title) > 0:
                movie.title = title

            # if release_date is available update it
            if len(release_date) > 0:
                movie.release_date = release_date

            movie = Movie(title=title, release_date=release_date)
            movie.insert()

            data = {
                'success': True,
                'movie': [movie.format_short()]
            }

            return jsonify(data)

        except Exception:
            abort(400)

    """
    Delete a movie from the id given in the url
    """
    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(payload, movie_id):
        try:
            # get the movie id from the url
            movie_id = int(movie_id)

            # fetch the movie with the id
            movie = Movie.query.filter(
                Movie.id == movie_id).one_or_none()

            # if no movie exists with that id, abort
            if movie is None:
                abort(400)

            movie.delete()

            data = {
                'success': True,
                'id': movie_id
            }

            return jsonify(data)

        except Exception:
            abort(400)

    """
    Create an actor. name, age, and gender are required.
    Returns the created actor as a list with one dictionary
    """
    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actor(payload):
        try:
            body = request.get_json()
            name = body.get('name', '')
            age = int(body.get('age', 0))
            gender = body.get('gender', '')

            # if any field is empty, abort
            if len(name) == 0 or age == 0 or len(gender) == 0:
                abort(400)

            # Capiutalize the first letter only: Male / Female / Other
            gender = gender.capitalize()

            actor = Actor(name=name, age=age, gender=gender)
            actor.insert()

            data = {
                'success': True,
                "actor": [actor.format_short()]
            }

            return jsonify(data)

        except Exception:
            abort(400)

    # format all actors and return the list
    def formatted_actors():
        # get all movies
        all_actors = Actor.query.order_by(Actor.id).all()
        formatted_actors = [
            actor.format() for actor in all_actors]
        return formatted_actors

    """
    Get the list of all actors
    """
    @app.route('/actors')
    @requires_auth('get:actors')
    def get_actors(payload):

        """
        This endpoint returns a list of all actors
        """
        try:
            data = {
                'success': True,
                'actors': formatted_actors()
            }

            # send data in json format
            return jsonify(data)

        except Exception:
            abort(404)

    """
    Update an actor. title or release_date required.
    Returns the updated actor as a list with one dictionary
    """
    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actor(payload, actor_id):
        try:
            # get the actor id from the url
            actor_id = int(actor_id)

            # fetch the actor with the id
            actor = Actor.query.filter(
                Actor.id == actor_id).one_or_none()

            # if no actor exists with that id, abort
            if actor is None:
                abort(400)

            # fetch the request body
            body = request.get_json()
            name = body.get('name', '')
            age = int(body.get('age', 0))
            gender = body.get('gender', '')

            # if all fields are empty, abort
            if len(name) == 0 and age == 0 and len(gender) == 0:
                abort(400)

            # if the field is available update it

            if len(name) > 0:
                actor.name = name

            if age > 0:
                actor.age = age

            if len(gender) > 0:
                # Capiutalize the first letter only: Male / Female / Other
                actor.gender = gender.capitalize()

            actor = Actor(name=name, age=age, gender=gender)
            actor.update()

            data = {
                "success": True,
                "actor": [actor.format_short()]
            }

            return jsonify(data)

        except Exception:
            abort(400)

    """
    Delete an actor from the id given in the url
    """
    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload, actor_id):
        try:
            # get the actor id from the url
            actor_id = int(actor_id)

            # fetch the actor with the id
            actor = Actor.query.filter(
                Actor.id == actor_id).one_or_none()

            # if no actor exists with that id, abort
            if actor is None:
                abort(400)

            actor.delete()

            data = {
                'success': True,
                'id': actor_id
            }

            return jsonify(data)

        except Exception:
            abort(400)

    """
    Users arrive to this endpoint after a successful login.
    User must note the access_token for further use.
    """
    @app.route('/login-results')
    def login_results():
        data = {
            "message": "Nice work! Now copy the access token from the url."
        }
        return jsonify(data)

    @app.route('/')
    def index():
        data = 'Welcome to Casting Agency! <br>\
            <a href="{}">Login</a>'.format(request_uri)
        return data

    '''
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    '''

    @app.errorhandler(400)
    def bad_request(error):
        data = {
            'success': False,
            'error': 400,
            'message': 'bad request'
        }
        return jsonify(data), 400

    @app.errorhandler(401)
    def bad_request(error):
        data = {
            'success': False,
            'error': 401,
            'message': 'unauthorized'
        }
        return jsonify(data), 401

    @app.errorhandler(404)
    def not_found(error):
        data = {
            'success': False,
            'error': 404,
            'message': 'resource not found'
        }
        return jsonify(data), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        data = {
            'success': False,
            'error': 405,
            'message': 'method not allowed'
        }
        return jsonify(data), 405

    @app.errorhandler(422)
    def unprocessable(error):
        data = {
            'success': False,
            'error': 422,
            'message': 'unprocessable'
        }
        return jsonify(data), 422

    @app.errorhandler(500)
    def internal_server_error(error):
        data = {
            'success': False,
            'error': 500,
            'message': 'internal server error'
        }
        return jsonify(data), 500

    return app


app = create_app()


if __name__ == '__main__':
    app.run()
