from flask import Blueprint, jsonify, request

from controllers import CNPJController

from api import BASE_API_URL

bp = Blueprint('cnpj', __name__, url_prefix=BASE_API_URL)

cnpj_controller = CNPJController()

@bp.route('/cnpjs', methods=['GET'])
def index():
    return cnpj_controller.all()


@bp.route('/cnpj/<int:id>', methods=['GET'])
def get_cnpj(id: int):
    return cnpj_controller.get(id)


@bp.route('/cnpj', methods=['POST'])
def create():
    return cnpj_controller.create(request)


@bp.route('/cnpj/<int:id>', methods=['DELETE'])
def delete(id: int):
    return cnpj_controller.delete(id)


@bp.route('/cnpj/<int:id>/block', methods=['PUT'])
def block(id: int):
    return cnpj_controller.block(id)


@bp.route('/cnpj/<int:id>/unblock', methods=['PUT'])
def unblock(id: int):
    return cnpj_controller.unblock(id)


@bp.route('/cnpj/validate', methods=['GET'])
def validate_cnpj():
    return cnpj_controller.validate(request)