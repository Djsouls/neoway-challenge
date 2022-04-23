from flask import Flask

def create_app() -> Flask:
    app = Flask('neoway-api')

    return app
