from flask import Flask
from src.transport.routes import user_bp



def create_app(config="../infrastructure/config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config)

    app.register_blueprint(user_bp)

    return app
