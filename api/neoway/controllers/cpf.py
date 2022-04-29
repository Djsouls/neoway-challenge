from flask import jsonify

from validate_docbr import CPF

from neoway.utils import clean_cpf

from neoway.controllers.decorators import format_response
from neoway.db.repositories import CPFRepository
from neoway.services.validator import validate

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
        # just for now
        cpf = clean_cpf(request.json.get('cpf'))

        if not validate(CPF(), cpf):
            return jsonify({'error': 'invalid cpf'}), 400

        return jsonify(self.repository.create(cpf))

    def delete(self, id: int):
        return jsonify(self.repository.delete(id))

    def block(self, id: int):
        cpf = self.repository.get(id)

        if cpf.blocked_at != None:
            return jsonify(cpf)

        return jsonify(self.repository.block(id))

    def unblock(self, id: int):
        return jsonify(self.repository.unblock(id))

    def get(self, id: int):
        return jsonify(self.repository.get(id) or [])

    def validate(self, request):
        ## TODO: Validate request params

        cpf = clean_cpf(request.args.get('cpf'))

        blocked = self.repository.blocked(cpf)
        print(blocked)
        return jsonify({
            'valid': validate(CPF(), cpf) and not blocked
        })