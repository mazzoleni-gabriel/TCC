from flask import current_app
from ..model import Github_repository

def list_all():
    return Github_repository.query.all()

def get_by_id(_id):
    return Github_repository.query.get(_id)

def save(repo):
    current = get_by_id(repo.github_id)
    if(current is None):
        return __save(repo)
    return repo

def __save(repo):
    current_app.db.session.add(repo)
    current_app.db.session.commit()
    return repo
