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
    hireable = db.Column(db.Boolean)
    github_created_at = db.Column(db.DateTime)
    extracted = db.Column(db.Boolean, default=False)

class Github_repository(db.Model):
    __tablename__ = "github_repository"
    github_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    full_name = db.Column(db.Text)
    language = db.Column(db.Text)
    is_fork = db.Column(db.Boolean)
    github_created_at = db.Column(db.DateTime)

class Github_pull_request(db.Model):
    __tablename__ = "github_pull_request"
    github_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    state = db.Column(db.Text)
    additions = db.Column(db.Integer)
    deletions = db.Column(db.Integer)
    github_created_at = db.Column(db.DateTime)
    github_closed_at = db.Column(db.DateTime)
    is_merged = db.Column(db.Boolean)
    github_merged_at = db.Column(db.DateTime)
    repository_id = db.Column(db.Integer, db.ForeignKey('github_repository.github_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('github_user.github_id'))

class Metrics(db.Model):
    __tablename__ = "metrics"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id_1 = db.Column(db.Integer, db.ForeignKey('github_user.github_id'))
    user_id_2 = db.Column(db.Integer, db.ForeignKey('github_user.github_id'))
    shared_repositories = db.Column(db.Float) # SR
    shared_contributions = db.Column(db.Float) # JCSR
    shared_pulls = db.Column(db.Float) # JCORS
