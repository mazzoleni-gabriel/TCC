from flask import current_app
from ..model import Token
from .. import model




def list_all():
    return Token.query.all()

def get_by_id(id):
    return Token.query.get(id)

def save(token):
    current_app.db.session.add(token)
    current_app.db.session.commit()
    return token

def update(id, token):
    query  = Token.query.filter(Token.id == id)
    query.update(token)
    current_app.db.session.commit()
    return query.first()

def delete(id):
    Token.query.filter(Token.id == id).delete()
    current_app.db.session.commit()

def get_first_expirated():
    return current_app.db.session.query(Token).order_by(Token.last_expiration).first()
