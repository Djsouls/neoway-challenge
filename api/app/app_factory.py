from flask import Flask
from flask_cors import CORS

def create_app() -> Flask:
    app = Flask('neoway-api')
    CORS(app)

    return app
