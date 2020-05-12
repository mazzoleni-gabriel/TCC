from flask import current_app
from ..model import Metrics

def list_all():
    return Metrics.query.all()

def get_by_id(_id):
    return Metrics.query.get(_id)

def save(metric):
    current_app.db.session.add(metric)
    current_app.db.session.commit()
    return metric
