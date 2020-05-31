from flask import Blueprint
from ..service import metrics_service, graph_service, semantic_metrics_service
import time

bp_metrics = Blueprint('metrics', __name__)

@bp_metrics.route('/metrics/shared-repos', methods=['POST'])
def calculate_shared_repos():
    start_time = time.time()
    metrics_service.calculate_shared_repos()
    print("--- shared-repos time:  %s seconds ---" % (time.time() - start_time))
    return '', 200

@bp_metrics.route('/metrics/topological/<login>', methods=['POST'])
def init_graph(login):
    start_time = time.time()
    graph_service.load_graph(login)
    print("--- topological metrics time:  %s seconds ---" % (time.time() - start_time))
    return '', 200

@bp_metrics.route('/metrics/shared_contributions/<login>', methods=['POST'])
def calculate_shared_contributions(login):
    start_time = time.time()
    semantic_metrics_service.save_shared_contributions(login)
    print("--- shared_contributions time:  %s seconds ---" % (time.time() - start_time))
    return '', 200

@bp_metrics.route('/metrics/shared_pulls/<login>', methods=['POST'])
def calculate_shared_pulls(login):
    start_time = time.time()
    semantic_metrics_service.save_shared_pulls(login)
    print("--- shared_pulls time:  %s seconds ---" % (time.time() - start_time))
    return '', 200