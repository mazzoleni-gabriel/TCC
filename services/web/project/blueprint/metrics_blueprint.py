from flask import Blueprint
from ..service import metrics_service, graph_service, semantic_metrics_service

bp_metrics = Blueprint('metrics', __name__)

@bp_metrics.route('/metrics/shared-repos', methods=['POST'])
def calculate_shared_repos():
    metrics_service.calculate_shared_repos()
    return '', 200

@bp_metrics.route('/graph/init/<login>', methods=['POST'])
def init_graph(login):
    graph_service.load_graph(login)
    return '', 200

@bp_metrics.route('/metrics/shared_contributions/<login>', methods=['POST'])
def calculate_shared_contributions(login):
    semantic_metrics_service.save_shared_contributions(login)
    return '', 200

@bp_metrics.route('/metrics/shared_pulls/<login>', methods=['POST'])
def calculate_shared_pulls(login):
    semantic_metrics_service.save_shared_pulls(login)
    return '', 200