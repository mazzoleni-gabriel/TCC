from flask import Blueprint
from ..service import metrics_service

bp_metrics = Blueprint('metrics', __name__)

@bp_metrics.route('/metrics/shared-repos', methods=['POST'])
def calculate_shared_repos():
    metrics_service.calculate_shared_repos()
    return '', 200