from flask import Blueprint, jsonify

from api import BASE_API_URL

from controllers import StatusController
from extensions import db

bp = Blueprint('api', __name__, url_prefix=BASE_API_URL)

status_controller = StatusController()

@bp.route('/')
def hello():
    return jsonify({'data': True})


@bp.route('/status')
def uptime():
    return status_controller.uptime()