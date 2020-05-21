from flask import Blueprint
from ..service import metrics_service, graph_service

bp_metrics = Blueprint('metrics', __name__)

@bp_metrics.route('/metrics/shared-repos', methods=['POST'])
def calculate_shared_repos():
    metrics_service.calculate_shared_repos()
    return '', 200

@bp_metrics.route('/graph/init/<login>', methods=['POST'])
def init_graph(login):
    graph_service.load_graph(login)
    return '', 200
