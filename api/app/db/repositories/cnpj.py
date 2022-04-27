from models import CNPJModel

class CNPJRepository:
    def __init__(self):
        self.model = CNPJModel

    def all(self):
        return self.model.query.all()