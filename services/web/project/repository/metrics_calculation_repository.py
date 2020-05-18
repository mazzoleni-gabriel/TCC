from flask import current_app
from sqlalchemy.sql import text
from ..model import Metrics

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