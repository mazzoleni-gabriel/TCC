from flask import current_app
from sqlalchemy.sql import text
from ..model import Metrics

def list_all():
    return Metrics.query.all()

def get_by_id(_id):
    return Metrics.query.get(_id)

def get_by_users_ids(user_id1, user_id2):
    query = text("""select * from metrics where
        (user_id_1 = :user1 and user_id_2 = :user2)
        or (user_id_1 = :user2 and user_id_2 = :user1)
        limit 1 """)
    result = current_app.db.session.query(Metrics).from_statement(query).params(user1=user_id1, user2 = user_id2).first()
    return result

def save(metric):
    found_metric = get_by_users_ids(metric.user_id_1, metric.user_id_2)
    if found_metric is not None:
        print("Metric already exists for users " + str(metric.user_id_1) + " and " + str(metric.user_id_2))
        return found_metric
    current_app.db.session.add(metric)
    current_app.db.session.commit()
    return metric

