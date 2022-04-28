import uuid

from sqlalchemy import Column, String, DECIMAL
from sqlalchemy.orm import declarative_base

from ext import db

def get_uuid():
    return uuid.uuid4().hex

class Car(db.Model):
    __tablename__ = 'car'

    id = Column(String(32), default=get_uuid, primary_key=True)
    carname = Column(String(32), unique=False, nullable=False)
    price = Column(DECIMAL(20, 2), default=0.00)

    def __str__(self):
        return self.id

    def __repr__(self):
        return self.carname