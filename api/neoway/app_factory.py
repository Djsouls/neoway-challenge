from flask import Flask

from dynaconf import FlaskDynaconf

from neoway.extensions import cors, db
from neoway.api import base, cpf, cnpj

def create_app() -> Flask:
    app = Flask('neoway-api')

    register_extensions(app)
    register_blueprints(app)

    return app

def register_extensions(app: Flask):
    FlaskDynaconf(app)
    cors.init_app(app)
    db.init_app(app)

def register_blueprints(app: Flask):
    app.register_blueprint(base.bp)
    app.register_blueprint(cpf.bp)
    app.register_blueprint(cnpj.bp)