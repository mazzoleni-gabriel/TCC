from flask import current_app
from ..model import Github_repository
from sqlalchemy.sql import text

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

def set_extracted(repo_id):
    session = current_app.db.session
    repo = session.query(Github_repository).\
        filter(Github_repository.github_id == repo_id).\
        first()
    if repo is not None:
        repo.extracted = True
        session.commit()

def is_extracted(repo_id):
    return get_by_id(repo_id).extracted

def get_repos_by_user(user_name):
    query = text("""select distinct r.* from github_user u
            join github_pull_request p on u.github_id = p.user_id
            join github_repository r on r.github_id = p.repository_id
            where u.login = :val""")
    result = current_app.db.session.query(Github_repository).from_statement(query).params(val=user_name).all()
    return result
