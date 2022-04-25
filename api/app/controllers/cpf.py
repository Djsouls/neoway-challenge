from flask import jsonify

from db.repositories import CPFRepository

class CPFController:
    def __init__(self):
      self.repository = CPFRepository()

    def get(self, id: int):
        return jsonify(self.repository.get(id))