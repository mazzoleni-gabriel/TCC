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
        return found_metric
    current_app.db.session.add(metric)
    current_app.db.session.commit()
    return metric

def update_adamic(user_id1, user_id2, adamic):
    query = text("""select * from metrics where
        (user_id_1 = :user1 and user_id_2 = :user2)
        or (user_id_1 = :user2 and user_id_2 = :user1)
        limit 1 """)
    session = current_app.db.session
    metric = current_app.db.session.query(Metrics).from_statement(query).params(user1=user_id1, user2 = user_id2).first()
    metric.adamic_adar = adamic
    session.commit()

def update_jaccard(user_id1, user_id2, jaccard):
    query = text("""select * from metrics where
        (user_id_1 = :user1 and user_id_2 = :user2)
        or (user_id_1 = :user2 and user_id_2 = :user1)
        limit 1 """)
    session = current_app.db.session
    metric = current_app.db.session.query(Metrics).from_statement(query).params(user1=user_id1, user2 = user_id2).first()
    metric.jaccard_coefficient = jaccard
    session.commit()

def update_resource_allocation(user_id1, user_id2, resource_allocation):
    query = text("""select * from metrics where
        (user_id_1 = :user1 and user_id_2 = :user2)
        or (user_id_1 = :user2 and user_id_2 = :user1)
        limit 1 """)
    session = current_app.db.session
    metric = current_app.db.session.query(Metrics).from_statement(query).params(user1=user_id1, user2 = user_id2).first()
    metric.resource_allocation = resource_allocation
    session.commit()

def update_shared_contributions(user_id1, user_id2, shared_contributions):
    query = text("""select * from metrics where
        (user_id_1 = :user1 and user_id_2 = :user2)
        or (user_id_1 = :user2 and user_id_2 = :user1)
        limit 1 """)
    session = current_app.db.session
    metric = current_app.db.session.query(Metrics).from_statement(query).params(user1=user_id1, user2 = user_id2).first()
    metric.shared_contributions = shared_contributions
    session.commit()

def update_shared_pulls(user_id1, user_id2, shared_pulls):
    query = text("""select * from metrics where
        (user_id_1 = :user1 and user_id_2 = :user2)
        or (user_id_1 = :user2 and user_id_2 = :user1)
        limit 1 """)
    session = current_app.db.session
    metric = current_app.db.session.query(Metrics).from_statement(query).params(user1=user_id1, user2 = user_id2).first()
    metric.shared_pulls = shared_pulls
    session.commit()


def get_metrics_with_SR(user_id):
    query = text("""select * from metrics where
        (user_id_1 = :user_id or user_id_2 = :user_id)
        and shared_repositories > 0 """)
    result = current_app.db.session.query(Metrics).from_statement(query).params(user_id=user_id).all()
    return result