from flask import current_app
from ..model import Github_pull_request

def list_all():
    return Github_pull_request.query.all()

def get_by_id(_id):
    return Github_pull_request.query.get(_id)

def save(pull):
    current = get_by_id(pull.github_id)
    if(current is None):
        return __save(pull)
    return pull

def __save(pull):
    current_app.db.session.add(pull)
    current_app.db.session.commit()
    return pull
