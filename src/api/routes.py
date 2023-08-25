"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, Movies, Extras
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/movie/<int:id>', methods=['GET'])
def get_movie(id):
    print(id)
    result = Movies.query.filter_by(movie_id=id).first()
    if result:
        return result.serialize()
    else:
        return jsonify({"mensaje":"Película no encontrada"})
    
@api.route('/extras/<int:id>', methods=['GET'])
def get_extras(id):
    result = Extras.query.filter_by(movie_id=id).all()
    result = list(map(lambda x: x.serialize(), result))

    if result:
        return result
    else:
        return jsonify({"mensaje":"Extras no encontrados"})

@api.route('/movie/add', methods=['POST'])
def add_movie():
    body = request.get_json()
    movie_exists = Movies.query.filter_by(tmdb_id=body["tmdb_id"]).first()

    if movie_exists:
        return jsonify({"mensaje":"Ese ID de TMDB ya existe en la base de datos"})
    else:
        movie = Movies(movie_title=body["movie_title"], movie_director=body["movie_director"], movie_runtime=body["movie_runtime"],movie_cast=body["movie_cast"],movie_audio_lang=body["movie_audio_lang"],movie_subs_lang=body["movie_subs_lang"],tmdb_id=body["tmdb_id"])
        db.session.add(movie)
        db.session.commit()

        return jsonify({"mensaje": "Película añadida a la base de datos"})

@api.route('/extras/add', methods=['POST'])
def add_extras():
    body = request.get_json()
    extras = Extras(extras_title=body["extras_title"],extras_description=body["extras_description"],extras_runtime=body["extras_runtime"],extras_audio_lang=body["extras_audio_lang"],extras_subs_lang=body["extras_subs_lang"],movie_id=body["movie_id"])
    db.session.add(extras)
    db.session.commit()

    return jsonify({"mensaje": "Extra añadido a la base de datos"})

