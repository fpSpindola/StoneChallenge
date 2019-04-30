from flask import Flask
from api.configs import Config
from api.funcionarios.routes import funcionarios

def create_app():
    config = Config.load_from_env()
    app = Flask(__name__)
    app.register_blueprint(funcionarios)
    return app, config
