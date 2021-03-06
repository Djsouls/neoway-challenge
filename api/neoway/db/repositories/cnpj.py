from datetime import datetime

from neoway.models import CNPJModel

from neoway.extensions import db

class CNPJRepository:
    def __init__(self):
      self.model = CNPJModel

    def all(self):
        return self.model.query.all()

    def get(self, id: int):
        return self.model.query.get(id)

    def create(self, cnpj: str = '12312312323'):
        cnpj = CNPJModel(cnpj=cnpj)

        db.session.add(cnpj)
        db.session.commit()

        return cnpj

    def delete(self, id: int):
        cnpj = self.model.query.get(id)

        if not cnpj:
            return []

        db.session.delete(cnpj)
        db.session.commit()

        return cnpj

    def block(self, id: int):
        cnpj = self.model.query.get(id)

        cnpj.blocked_at = datetime.now()

        db.session.commit()

        return cnpj

    def unblock(self, id: int):
        cnpj = self.model.query.get(id)

        if cnpj is None:
            return []

        cnpj.blocked_at = None

        db.session.commit()

        return cnpj

    def blocked(self, cnpj: str):
        cnpj = self.model.query.filter_by(cnpj=cnpj).first()

        return False if cnpj == None else cnpj.blocked_at != None