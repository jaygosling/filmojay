from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Movies(db.Model):
    movie_id = db.Column(db.Integer, primary_key=True)
    movie_title = db.Column(db.String(120), unique=True, nullable=False)
    movie_director = db.Column(db.String(80), unique=False, nullable=False)
    movie_cast = db.Column(db.String(255), unique=False, nullable=False)
    movie_runtime = db.Column(db.Integer, unique=False, nullable=False)
    movie_audio_lang = db.Column(db.String(255), unique=False, nullable=False)
    movie_subs_lang = db.Column(db.String(255), unique=False, nullable=False)
    tmdb_id = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return f'<Movies {self.movie_title}>'

    def serialize(self):
        return {
            "id": self.movie_id,
            "movie_title": self.movie_title,
            "movie_director": self.movie_director,
            "movie_cast": self.movie_cast,
            "movie_runtime": self.movie_runtime,
            "movie_audio_lang": self.movie_audio_lang,
            "movie_subs_lang": self.movie_subs_lang,
            "tmdb_id": self.tmdb_id
            # do not serialize the password, its a security breach
        }
class Extras(db.Model):
    extras_id = db.Column(db.Integer, primary_key=True)
    extras_title = db.Column(db.String(120), unique=True, nullable=False)
    extras_description = db.Column(db.String(500), unique=False, nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'))
    extras_runtime = db.Column(db.Integer, unique=False, nullable=False)
    extras_audio_lang = db.Column(db.String(255), unique=False, nullable=False)
    extras_subs_lang = db.Column(db.String(255), unique=False, nullable=False)
    rel_movie = db.relationship(Movies)

    def __repr__(self):
        return f'<Extras {self.extras_title}>'

    def serialize(self):
        return {
            "id": self.extras_id,
            "extras_title": self.extras_title,
            "extras_description": self.extras_description,
            "extras_runtime": self.extras_runtime,
            "extras_audio_lang": self.extras_audio_lang,
            "extras_subs_lang": self.extras_subs_lang,
            "movie_id": self.movie_id
            # do not serialize the password, its a security breach
        }

class Languages(db.Model):
    lang_id = db.Column(db.Integer, primary_key=True)
    lang_code = db.Column(db.String(120), unique=True, nullable=False)
    lang_name = db.Column(db.String(500), unique=False, nullable=False)
    
    def __repr__(self):
        return f'<Languages {self.lang_name}>'

    def serialize(self):
        return {
            "lang_id": self.lang_id,
            "lang_code": self.lang_code,
            "lang_name": self.lang_name
            # do not serialize the password, its a security breach
        }
