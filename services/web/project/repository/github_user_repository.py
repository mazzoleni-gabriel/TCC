from flask import current_app
from ..model import Github_user

def list_all():
    return Github_user.query.all()

def get_by_id(_id):
    return Github_user.query.get(_id)

def get_by_login(login):
    return current_app.db.session.query(Github_user).\
        filter(Github_user.login == login).\
        first()

def save(github_user):
    current = get_by_id(github_user.github_id)
    if(current is None):
        return __save(github_user)
    return github_user

def __save(github_user):
    current_app.db.session.add(github_user)
    current_app.db.session.commit()
    return github_user

def update(github_id, github_user):
    query  = Github_user.query.filter(Github_user.github_id == github_id)
    query.update(github_user)
    current_app.db.session.commit()
    return query.first()
