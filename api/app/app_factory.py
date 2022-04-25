from flask import Flask

from extensions import cors

from api import resources, cpf

def create_app() -> Flask:
    app = Flask('neoway-api')

    register_extensions(app)
    register_blueprints(app)

    return app

def register_extensions(app: Flask):
    cors.init_app(app)

def register_blueprints(app: Flask):
    app.register_blueprint(resources.bp)
    app.register_blueprint(cpf.bp)