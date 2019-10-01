from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_moment import Moment


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
bootstrap = Bootstrap()
moment = Moment()

def create_app(config):

    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    login.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)


    from app.actor import bp as actor_bp
    app.register_blueprint(actor_bp)

    from app.movie import bp as movie_bp
    app.register_blueprint(movie_bp)

    from app.user import bp as user_bp
    app.register_blueprint(user_bp)

    from app.error import bp as error_bp
    app.register_blueprint(error_bp)

    return app


app = create_app(Config)

from app import models, routes






