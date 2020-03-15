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

class Github_user(db.Model):
    __tablename__ = "github_user"
    github_id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.Text)
    name = db.Column(db.Text)
    avatar_url = db.Column(db.Text)
    location = db.Column(db.Text)
    bio = db.Column(db.Text)
    email = db.Column(db.Text)
    hireable = db.Column(db.Boolean) #
    github_created_at = db.Column(db.DateTime)
