from flask import Blueprint, jsonify, request

from controllers import CPFController

from services.cpf_validator import CPFValidator

from db.repositories import CPFRepository

from api import BASE_API_URL

bp = Blueprint('cpf', __name__, url_prefix=BASE_API_URL)

cpf_controller = CPFController()

@bp.route('/cpfs', methods=['GET'])
def index():
    return cpf_controller.all()


@bp.route('/cpf/test')
def test():
    return cpf_controller.test_format_response()


@bp.route('/cpf/<int:id>', methods=['GET'])
def get_cpf(id: int):
    return cpf_controller.get(id)


@bp.route('/cpf', methods=['POST'])
def create():
    return cpf_controller.create(request)


@bp.route('/validate', methods=['GET', 'POST'])
def validate_cpf():
    return jsonify({
        'valid': CPFValidator.perform('11122255525')
    })