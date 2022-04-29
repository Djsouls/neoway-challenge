from flask import jsonify

from validate_docbr import CPF

from neoway.utils import clean_cpf

from neoway.controllers.decorators import format_response

from neoway.db.repositories import CPFRepository
from neoway.services.validator import validate_cpf

class CPFController:
    def __init__(self):
        self.repository = CPFRepository()

    @format_response
    def all(self):
        result = self.repository.all()

        return {
            'count': len(result),
            'results': result,
            'success': True
        }

    def create(self, request):
        ## TODO: Validate request params
        cpf = clean_cpf(request.json.get('cpf'))

        if not validate_cpf(cpf):
            return jsonify({'error': 'invalid cpf'}), 400

        return jsonify(self.repository.create(cpf))

    def delete(self, id: int):
        response = self.repository.delete(id)

        return jsonify(response) if response == [] else jsonify(response), 400

    def block(self, id: int):
        cpf = self.repository.get(id)

        if cpf is None:
            return jsonify([]), 400

        if cpf.blocked_at != None:
            return jsonify(cpf)

        return jsonify(self.repository.block(id))

    def unblock(self, id: int):
        response = self.repository.unblock(id)

        return jsonify(response) if response == [] else jsonify(response), 400

    def get(self, id: int):
        return jsonify(self.repository.get(id) or [])

    def validate(self, request):
        ## TODO: Validate request params

        cpf = clean_cpf(request.args.get('cpf'))

        blocked = self.repository.blocked(cpf)
        print(blocked)
        return jsonify({
            'valid': validate_cpf(cpf) and not blocked
        })