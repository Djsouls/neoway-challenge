from flask import jsonify

from validate_docbr import CNPJ

from neoway.utils import clean_cnpj

from neoway.controllers.decorators import format_response
from neoway.db.repositories import CNPJRepository
from neoway.services.validator import validate

class CNPJController:
    def __init__(self):
        self.repository = CNPJRepository()

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
        cnpj = clean_cnpj(request.json.get('cnpj'))

        if not validate(CNPJ(), cnpj):
            return jsonify({'error': 'invalid cnpj'}), 400

        return jsonify(self.repository.create(cnpj))

    def delete(self, id: int):
        return jsonify(self.repository.delete(id))

    def block(self, id: int):
        cnpj = self.repository.get(id)

        if cnpj.blocked_at != None:
            return jsonify(cnpj)

        return jsonify(self.repository.block(id))

    def unblock(self, id: int):
        return jsonify(self.repository.unblock(id))

    def get(self, id: int):
        return jsonify(self.repository.get(id) or [])

    def validate(self, request):
        ## TODO: Validate request params

        cnpj = clean_cnpj(request.args.get('cnpj'))

        blocked = self.repository.blocked(cnpj)

        return jsonify({
            'valid': validate(CNPJ(), cnpj) and not blocked
        })