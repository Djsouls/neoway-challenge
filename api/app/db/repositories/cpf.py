from models import CPFModel

from extensions import db

class CPFRepository:
    def __init__(self):
      self.model = CPFModel

    def all(self):
        return self.model.query.all()

    # TODO: Implement return type, see types in SQLAlchemy ORM docs
    def get(self, id: int):
        return self.model.query.get(id)

    # TODO: Implement args getting dinamic (**args)
    def create(self, cpf: str = '12312312323'):
        cpf = CPFModel(cpf=cpf)

        db.session.add(cpf)
        db.session.commit()

        return cpf