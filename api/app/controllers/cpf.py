from controllers.decorators import format_response

from db.repositories import CPFRepository

from flask import jsonify

class CPFController:
    def __init__(self):
        self.repository = CPFRepository()

    @format_response
    def all(self):
        result = self.repository.all()

        return {
            'count': len(result),
            'data': result,
            'success': True
        }

    def create(self, request):
        ## TODO: Validate request params
        # just for now
        cpf = request.json.get('cpf')

        return jsonify(self.repository.create(cpf))

    def get(self, id: int):
        return jsonify(self.repository.get(id) or [])