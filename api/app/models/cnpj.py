from dataclasses import dataclass
from datetime import datetime

from extensions import db

@dataclass
class CNPJModel(db.Model):
    __tablename__ = 'cnpjs'

    id: int = db.Column(db.Integer, db.Identity(), primary_key=True)
    cnpj: str = db.Column(db.String, nullable=False)

    blocked_at: datetime = db.Column(db.DateTime, default=None)
    created_at: datetime = db.Column(db.DateTime, default=datetime.now(),
        nullable=False)