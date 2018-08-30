from flask import Flask
from flask_bootstrap import Bootstrap

from .config import DevConfig




# Initalize the app
app = Flask(__name__)


# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('../instance/config.py')
bootstrap = Bootstrap(app)

from app import views
from app import error
