from flask import Flask
from app.config import app_config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    return app
