from flask import current_app
from ..model import Token


def list_all():
    return Token.query.all()

def get_by_id(_id):
    return Token.query.get(_id)

def save(token):
    current_app.db.session.add(token)
    current_app.db.session.commit()
    return token

def update(_id, token):
    session = current_app.db.session
    query  = session.query(Token).filter(Token.id == _id)
    query.update(token)
    session.commit()
    return query.first()

def delete(_id):
    Token.query.filter(Token.id == _id).delete()
    current_app.db.session.commit()

def get_first_expirated():
    return current_app.db.session.query(Token).\
        order_by(Token.last_expiration).\
        first()

def update_last_expiration(_id, new_expiration):
    session = current_app.db.session
    token  = session.query(Token).filter(Token.id == _id).first()
    token.last_expiration = new_expiration
    session.commit()
    return token
