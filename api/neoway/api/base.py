from flask import Blueprint, jsonify

from neoway.api import BASE_API_URL

from neoway.controllers import StatusController
from neoway.extensions import db

bp = Blueprint('api', __name__, url_prefix=BASE_API_URL)

status_controller = StatusController()

@bp.route('/')
def hello():
    return jsonify({'hello': 'world'})


@bp.route('/status')
def uptime():
    return status_controller.uptime()