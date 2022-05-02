import uuid

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def get_uuid():
    return uuid.uuid4().hex
