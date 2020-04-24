'''
Tests for casting agency
'''
# import os
import json
import pytest
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db

from env_file import test_database_path

"""
CA_TOKEN = ""
CD_TOKEN = ''
EP_TOKEN = ''
"""
CA_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImloNEtoY2RiTnFvbkxTamN0ZnN5ViJ9.eyJpc3MiOiJodHRwczovL3RoZWNhc3RpbmdhZ2VuY3kuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYTE4OTgzMDhjYTEwMGM2ZGViMTUxNSIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTU4NzcwNzY3MiwiZXhwIjoxNTg3Nzk0MDcyLCJhenAiOiJPUm5MQUQwTU9yY3pwejRtYXYwRWh6ck1oTFpERFE4biIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.pklBCcNTjlMcggl0Fb4yBZ06eSSLBR8E4Yvc4WcTYUZqZlKW1dmda-mplKxOheRaMqWfBr8xHCe2qkDsGvCnPcqv0Y2B8jfLzhybgWdYUMyCrPpy3HHC92p6ZpAea1tXEbztqYW7IxbE83Jq3OrSUfssE-RLFiWHD8JcmZ3nbtZCojGT6P339JKz2tJcmCp5DZx1zxkiVYOP98jwhPPmpPA_U3Zi3O5l1YErhbMtrSwwZiZQ4EIqSMgb4d67Lp30wMr3CWeasVunX6T2sjwLVWqqLF-t-6uqH3K7hw-3XGLsRW146XF3RUhcYMGIkh5j0eR0ageaF44Y47_7lDKMyQ"
CD_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImloNEtoY2RiTnFvbkxTamN0ZnN5ViJ9.eyJpc3MiOiJodHRwczovL3RoZWNhc3RpbmdhZ2VuY3kuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYTE5NTkxZmVjNGQwMGUxZDViNzJmNCIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTU4NzcwNzczOSwiZXhwIjoxNTg3Nzk0MTM5LCJhenAiOiJPUm5MQUQwTU9yY3pwejRtYXYwRWh6ck1oTFpERFE4biIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.n4ZZ9h2CwcnmwqloWrtZqSmok7TApRBDpUqTudFtckRCFUoNi56tuglImY1eXkxxw82iZabIrDJW32SWQoDaCoq9zFyNO57oEpPOdoiFLkhhQ9ho6N6cfALwduvG3HcbkukSjsCdM1awsVx8rbV17JQzbr899eADyV_SD0csGoJW8o6qYYQ-k_l8btPAifCclH2PuvcLxkdB2zlSIQNzazmPIyOQPi8iAMCQH1HH7dnJ2au3L_loXyQSycYVkBksK2cf0NlctWhYzUSpJukeyDxIZCPWkOANVqBAc9ARTAmlPdM-vfSYzFFPhSjn09sXKVYVDKOr_6Ewksg8gc1bkg'
EP_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImloNEtoY2RiTnFvbkxTamN0ZnN5ViJ9.eyJpc3MiOiJodHRwczovL3RoZWNhc3RpbmdhZ2VuY3kuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYTE5NTU4ZmVjNGQwMGUxZDViNzI0MyIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTU4NzcwNzgxMiwiZXhwIjoxNTg3Nzk0MjEyLCJhenAiOiJPUm5MQUQwTU9yY3pwejRtYXYwRWh6ck1oTFpERFE4biIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.Vid-zqaH-8AOzeVvT4GBOOm4SVfaM3sIz4in8Y9GUJ7Y-qNZdFWja0Nbz2Wqo3m0TOiBcgkCL7jElnqd_mM0mzmyLHIrijegGRRrbHDNEvSCJNPXQ_fGvpDJIYPEBRzFoD5j8mrymN51nCVNV7XH9LWPc2rWvkNzFMrvkqavForHLdDd2EEovLdP4pU59XzlwrbAFu2VoD8FYVW9iJRatRKfB_aL3LVoFEFonQwWQeyxI2Q92okxh5HnHGoGIUp0mHBV-xGZAxZ4va453D2SX1aExlRlac-YfHeGIxG0xtkAJ86JRj33DWI400UhmCQuF-bTeeVVU9DC3SkUVjhqew'

movie_id = 1
actor_id = 1


@pytest.fixture
def client():
    app = create_app()
    client = app.test_client()

    setup_db(app, test_database_path)

    with app.app_context():
        db = SQLAlchemy()
        db.init_app(app)

        # create all tables
        db.create_all()

    yield client


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200


"""
Executive Producer Movies
"""


# Test Executive Producer Create Movie
def test_ep_create_movies(client):
    headers = {
        'Authorization': 'Bearer {}'.format(EP_TOKEN)
    }

    body = {
        "title": "movie1",
        "release_date": "2020-10-20"
    }

    response = client.post(
        '/movies',
        headers=headers,
        data=json.dumps(body),
        content_type='application/json'
    )

    assert response.status_code == 200
    movie = response.json['movie']
    assert type(movie) is list


# Test Executive Producer Get Movies
def test_ep_get_movies(client):
    headers = {
        'Authorization': 'Bearer {}'.format(EP_TOKEN)
    }

    response = client.get(
        '/movies',
        headers=headers
    )

    assert response.status_code == 200
    movies = response.json['movies']
    assert type(movies) is list


# Test Executive Producer Update Movie
def test_ep_update_movies(client):
    headers = {
        'Authorization': 'Bearer {}'.format(EP_TOKEN)
    }

    body = {
        "title": "movie1_update",
        "release_date": "2020-12-20"
    }

    response = client.patch(
        '/movies/{}'.format(movie_id),
        headers=headers,
        data=json.dumps(body),
        content_type='application/json'
    )

    assert response.status_code == 200
    movie = response.json['movie']
    assert type(movie) is list


"""
Casting Director Movies
"""


# Test Casting Director Create Movie
def test_cd_create_movies(client):
    headers = {
        'Authorization': 'Bearer {}'.format(CD_TOKEN)
    }

    body = {
        "title": "movie1",
        "release_date": "2020-10-20"
    }

    response = client.post(
        '/movies',
        headers=headers,
        data=json.dumps(body),
        content_type='application/json'
    )

    assert response.status_code == 401


# Test Casting Director Get Movies
def test_cd_get_movies(client):
    headers = {
        'Authorization': 'Bearer {}'.format(CD_TOKEN)
    }

    response = client.get(
        '/movies',
        headers=headers
    )

    assert response.status_code == 200
    movies = response.json['movies']
    assert type(movies) is list


# Test Casting Director Update Movie
def test_cd_update_movies(client):
    headers = {
        'Authorization': 'Bearer {}'.format(CD_TOKEN)
    }

    body = {
        "title": "movie1_update",
        "release_date": "2020-12-20"
    }

    response = client.patch(
        '/movies/{}'.format(movie_id),
        headers=headers,
        data=json.dumps(body),
        content_type='application/json'
    )

    assert response.status_code == 200
    movie = response.json['movie']
    assert type(movie) is list


# Test Casting Director Delete Movie
def test_cd_delete_movies(client):
    headers = {
        'Authorization': 'Bearer {}'.format(CD_TOKEN)
    }

    response = client.delete(
        '/movies/{}'.format(movie_id),
        headers=headers
    )

    assert response.status_code == 401


"""
Casting Assistant Movies
"""


# Test Casting Assistant Create Movie
def test_ca_create_movies(client):
    headers = {
        'Authorization': 'Bearer {}'.format(CA_TOKEN)
    }

    body = {
        "title": "movie1",
        "release_date": "2020-10-20"
    }

    response = client.post(
        '/movies',
        headers=headers,
        data=json.dumps(body),
        content_type='application/json'
    )

    assert response.status_code == 401


# Test Casting Assistant Get Movies
def test_ca_get_movies(client):
    headers = {
        'Authorization': 'Bearer {}'.format(CA_TOKEN)
    }

    response = client.get(
        '/movies',
        headers=headers
    )

    assert response.status_code == 200
    movies = response.json['movies']
    assert type(movies) is list


# Test Casting Assistant Update Movie
def test_ca_update_movies(client):
    headers = {
        'Authorization': 'Bearer {}'.format(CA_TOKEN)
    }

    body = {
        "title": "movie1_update",
        "release_date": "2020-12-20"
    }

    response = client.patch(
        '/movies/{}'.format(movie_id),
        headers=headers,
        data=json.dumps(body),
        content_type='application/json'
    )

    assert response.status_code == 401


# Test Casting Assistant Delete Movie
def test_ca_delete_movies(client):
    headers = {
        'Authorization': 'Bearer {}'.format(CA_TOKEN)
    }

    response = client.delete(
        '/movies/{}'.format(movie_id),
        headers=headers
    )

    assert response.status_code == 401


"""
Executive Producer Actors
"""


# Test Executive Producer Create Actor
def test_ep_create_actors(client):
    headers = {
        'Authorization': 'Bearer {}'.format(EP_TOKEN)
    }

    body = {
        "name": "actor1",
        "age": 25,
        "gender": "female"
    }

    response = client.post(
        '/actors',
        headers=headers,
        data=json.dumps(body),
        content_type='application/json'
    )

    assert response.status_code == 200
    actor = response.json['actor']
    assert type(actor) is list


# Test Executive Producer Get Actors
def test_ep_get_actors(client):
    headers = {
        'Authorization': 'Bearer {}'.format(EP_TOKEN)
    }

    response = client.get(
        '/actors',
        headers=headers
    )

    assert response.status_code == 200
    actors = response.json['actors']
    assert type(actors) is list


# Test Executive Producer Update Actor
def test_ep_update_actors(client):
    headers = {
        'Authorization': 'Bearer {}'.format(EP_TOKEN)
    }

    body = {
        "name": "actor1",
        "age": 25,
        "gender": "female"
    }

    response = client.patch(
        '/actors/{}'.format(actor_id),
        headers=headers,
        data=json.dumps(body),
        content_type='application/json'
    )

    assert response.status_code == 200
    actor = response.json['actor']
    assert type(actor) is list


"""
Casting Director Actors
"""


# Test Casting Director Create Actor
def test_cd_create_actors(client):
    headers = {
        'Authorization': 'Bearer {}'.format(CD_TOKEN)
    }

    body = {
        "name": "actor1",
        "age": 25,
        "gender": "female"
    }

    response = client.post(
        '/actors',
        headers=headers,
        data=json.dumps(body),
        content_type='application/json'
    )

    assert response.status_code == 200
    actor = response.json['actor']
    assert type(actor) is list


# Test Casting Director Get Actors
def test_cd_get_actors(client):
    headers = {
        'Authorization': 'Bearer {}'.format(CD_TOKEN)
    }

    response = client.get(
        '/actors',
        headers=headers
    )

    assert response.status_code == 200
    actors = response.json['actors']
    assert type(actors) is list


# Test Casting Director Update Actor
def test_cd_update_actors(client):
    headers = {
        'Authorization': 'Bearer {}'.format(CD_TOKEN)
    }

    body = {
        "name": "actor1",
        "age": 25,
        "gender": "female"
    }

    response = client.patch(
        '/actors/{}'.format(actor_id),
        headers=headers,
        data=json.dumps(body),
        content_type='application/json'
    )

    assert response.status_code == 200
    actor = response.json['actor']
    assert type(actor) is list


"""
Casting Assistant Actors
"""


# Test Casting Assistant Create Actor
def test_ca_create_actors(client):
    headers = {
        'Authorization': 'Bearer {}'.format(CA_TOKEN)
    }

    body = {
        "name": "actor1",
        "age": 25,
        "gender": "female"
    }

    response = client.post(
        '/actors',
        headers=headers,
        data=json.dumps(body),
        content_type='application/json'
    )

    assert response.status_code == 401


# Test Casting Assistant Get Actors
def test_ca_get_actors(client):
    headers = {
        'Authorization': 'Bearer {}'.format(CA_TOKEN)
    }

    response = client.get(
        '/actors',
        headers=headers
    )

    assert response.status_code == 200
    actors = response.json['actors']
    assert type(actors) is list


# Test Casting Assistant Update Actor
def test_ca_update_actors(client):
    headers = {
        'Authorization': 'Bearer {}'.format(CA_TOKEN)
    }

    body = {
        "name": "actor1",
        "age": 25,
        "gender": "female"
    }

    response = client.patch(
        '/actors/{}'.format(actor_id),
        headers=headers,
        data=json.dumps(body),
        content_type='application/json'
    )

    assert response.status_code == 401


# Test Casting Assistant Delete Actor
def test_ca_delete_actors(client):
    headers = {
        'Authorization': 'Bearer {}'.format(CA_TOKEN)
    }

    response = client.delete(
        '/actors/{}'.format(actor_id),
        headers=headers
    )

    assert response.status_code == 401
