from flask import Blueprint, jsonify, request

from controllers import CPFController

from api import BASE_API_URL

bp = Blueprint('cpf', __name__, url_prefix=BASE_API_URL)

cpf_controller = CPFController()

@bp.route('/cpfs', methods=['GET'])
def index():
    return cpf_controller.all()


@bp.route('/cpf/<int:id>', methods=['GET'])
def get_cpf(id: int):
    return cpf_controller.get(id)


@bp.route('/cpf', methods=['POST'])
def create():
    return cpf_controller.create(request)


@bp.route('/cpf/<int:id>', methods=['DELETE'])
def delete(id: int):
    return cpf_controller.delete(id)


@bp.route('/cpf/<int:id>/block', methods=['PUT'])
def block(id: int):
    return cpf_controller.block(id)


@bp.route('/cpf/<int:id>/unblock', methods=['PUT'])
def unblock(id: int):
    return cpf_controller.unblock(id)


@bp.route('/cpf/validate', methods=['GET'])
def validate_cpf():
    return cpf_controller.validate(request)