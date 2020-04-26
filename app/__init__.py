from flask import Flask
from .config import DevConfig

#init app
app = Flask(__name__,instance_relative_config= True)

#setting config
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views