from flask import Flask
from api.configs import Config


def create_app():
    config = Config.load_from_env()
    app = Flask(__name__)
    return app, config
