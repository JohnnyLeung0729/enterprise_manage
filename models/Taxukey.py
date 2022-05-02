# coding: utf-8
from flask_sqlalchemy import SQLAlchemy

from ext import db, get_uuid


class Taxukey(db.Model):
    __tablename__ = 'taxukey'

    id = db.Column(db.String(32), primary_key=True, default=get_uuid, unique=True, info='ID')
    keytype = db.Column(db.Integer, nullable=False, info='税控Ukey类型')
    keyno = db.Column(db.String(32), info='税控Ukey号码')
    Enterprise_id = db.Column(db.ForeignKey('enterprise.id'), nullable=False, index=True)

    Enterprise = db.relationship('Enterprise', primaryjoin='Taxukey.Enterprise_id == Enterprise.id', backref='taxukeys')

    def __repr__(self):
        return self.keyno

    def __str__(self):
        return self.Enterprise_id