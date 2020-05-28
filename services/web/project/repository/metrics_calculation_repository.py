from flask import current_app
from sqlalchemy.sql import text

def shared_repos():
    query = text("""select u1.github_id as user_id_1,
                    u2.github_id as user_id_2,
                    count(distinct r.github_id) as shared_repositories
                    from github_user u1
                    join github_pull_request p on u1.github_id = p.user_id
                    join github_repository r on r.github_id = p.repository_id
                    join github_pull_request p2 on r.github_id = p2.repository_id
                    join github_user u2 on u2.github_id = p2.user_id group by u1.github_id, u2.github_id
                    having u1.github_id <> u2.github_id""")
    result = current_app.db.engine.execute(query)
    return result

def shared_repo_ids_by_users(user_id_1, user_id_2):
    query = text("""select distinct(r.github_id) as repo_id
                    from github_user u1
                    join github_pull_request p on u1.github_id = p.user_id
                    join github_repository r on r.github_id = p.repository_id
                    join github_pull_request p2 on r.github_id = p2.repository_id
                    join github_user u2 on u2.github_id = p2.user_id
                    where u1.github_id = :user_id1 and u2.github_id = :user_id2""")
    result = current_app.db.engine.execute(query, user_id1=user_id_1, user_id2=user_id_2)
    repo_ids = [ r.repo_id for r in result ]
    return repo_ids

def count_contributors(repo_id):
    query = text("""select count( distinct(p.user_id)) as repos_count
                    from github_repository r
                    join github_pull_request p on r.github_id = p.repository_id
                    where r.github_id = :repo_id""")
    result = current_app.db.engine.execute(query, repo_id=repo_id).first()
    return result.repos_count

def count_pulls_by_user_in_repo(repo_id, user_id):
    query = text("""select count(1) as pulls_count
                    from github_pull_request p
                    where p.repository_id = :repo_id and p.user_id = :user_id""")
    result = current_app.db.engine.execute(query, repo_id=repo_id, user_id=user_id).first()
    return result.pulls_count

def count_pulls_in_repo(repo_id):
    query = text("""select count(1) as pulls_count
                    from github_pull_request p
                    where p.repository_id = :repo_id""")
    result = current_app.db.engine.execute(query, repo_id=repo_id).first()
    return result.pulls_count