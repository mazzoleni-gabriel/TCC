from flask import Blueprint
from ..service import github_pull_request_extrator_service as service

bp_github_pull_request = Blueprint('github_pull_request', __name__)

@bp_github_pull_request.route('/github-pull-request/repo/<user>/<repo>', methods=['POST'])
def save_user_repos(user, repo):
    service.save_pulls_by_repo_name(user, repo)
    return '', 200
