from flask import Blueprint, jsonify

from api import BASE_API_URL

bp = Blueprint('api', __name__, url_prefix=BASE_API_URL)

@bp.route('/')
def hello():
    return jsonify({'data': True})
