from flask import current_app
from sqlalchemy import update
from ..model import Github_user
from sqlalchemy.sql import text

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

def set_extracted(login):
    session = current_app.db.session
    user = session.query(Github_user).\
        filter(Github_user.login == login).\
        first()
    user.extracted = True
    session.commit()

def get_non_extracted_neighbors(user_name):
    query = text("""select distinct u2.* from github_user u
            join github_pull_request p on u.github_id = p.user_id
            join github_repository r on r.github_id = p.repository_id
            join github_pull_request p2 on r.github_id = p2.repository_id
            join github_user u2 on u2.github_id = p2.user_id
            where u2.extracted = false
            and u.login = :val""")
    result = current_app.db.session.query(Github_user).from_statement(query).params(val=user_name).all()
    return result