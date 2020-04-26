from flask import Flask

#init app
app = Flask(__name__)

#setting config
app.config.from_object(DevConfig)

from app import views