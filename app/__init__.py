from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

#init app
app = Flask(__name__,instance_relative_config = True)

#setting config
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#initialized flask extensions
bootstrap = Bootstrap(app)

from app import views
from app import error