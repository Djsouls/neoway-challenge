from dataclasses import dataclass
from datetime import datetime

from extensions import db

@dataclass
class CPFModel(db.Model):
    __tablename__ = 'cpfs'

    id: int = db.Column(db.Integer, db.Identity(), primary_key=True)
    cpf: str = db.Column(db.String, nullable=False)

    blocked_at: datetime = db.Column(db.DateTime, default=None)
    created_at: datetime = db.Column(db.DateTime, default=datetime.now(),
        nullable=False)
    updated_at: datetime = db.Column(db.DateTime, default=datetime.now(),
        nullable=False)