from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db
    return db

class Token(db.Model):
    __tablename__ = "token"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token_value = db.Column(db.Text, nullable=False)
    last_expiration = db.Column(db.DateTime, default=datetime.utcnow)
