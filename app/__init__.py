from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from config import config_options

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    # Initalize the app
    app = Flask(__name__)

    # Setting up configuration
    app.config.from_object(config_options[config_name])
    app.config.from_pyfile('../instance/config.py')

    # app.config['SQLALCHEMY_DATABASES_URI'] = 'postgresql+psycopg2://vonmutinda:von@localhost/watchlist'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:password@localhost/watchlist'

    bootstrap.init_app(app)
    db.init_app(app)

    # Registering a Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # configuring requests
    from .request import config_requests
    config_requests(app)


    return app



# from app import views
# from app import error
