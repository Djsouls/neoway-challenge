from datetime import datetime

from neoway.models import CPFModel

from neoway.extensions import db

class CPFRepository:
    def __init__(self):
      self.model = CPFModel

    def all(self):
        return self.model.query.all()

    def get(self, id: int):
        return self.model.query.get(id)

    def create(self, cpf: str = '12312312323'):
        cpf = CPFModel(cpf=cpf)

        db.session.add(cpf)
        db.session.commit()

        return cpf

    def delete(self, id: int):
        cpf = self.model.query.get(id)

        if not cpf:
            return []

        db.session.delete(cpf)
        db.session.commit()

        return cpf

    def block(self, id: int):
        cpf = self.model.query.get(id)

        cpf.blocked_at = datetime.now()

        db.session.commit()

        return cpf

    def unblock(self, id: int):
        cpf = self.model.query.get(id)

        if cpf is None:
            return []

        cpf.blocked_at = None

        db.session.commit()

        return cpf

    def blocked(self, cpf: str):
        cpf = self.model.query.filter_by(cpf=cpf).first()

        return False if cpf == None else cpf.blocked_at != None