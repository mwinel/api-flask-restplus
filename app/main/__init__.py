from flask import Flask
from app.main.config import app_config
from app.main.models import user

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    return app
