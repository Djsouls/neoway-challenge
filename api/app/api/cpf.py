from flask import Blueprint, jsonify, request

from controllers import CPFController

from services.cpf_validator import CPFValidator

from db.repositories import CPFRepository

from api import BASE_API_URL

bp = Blueprint('cpf', __name__, url_prefix=BASE_API_URL + '/cpf')

cpf_controller = CPFController()

@bp.route('/', methods=['GET'])
def index():
    return 'ITS ALIVE'


@bp.route('/<int:id>', methods=['GET'])
def get_cpf(id: int):
    return cpf_controller.get(id)


@bp.route('/', methods=['POST'])
def create():
    created_cpf = cpf_controller.create(request)

    return jsonify(created_cpf)


@bp.route('/validate', methods=['GET', 'POST'])
def validate_cpf():
    return jsonify({
        'valid': CPFValidator.perform('11122255525')
    })