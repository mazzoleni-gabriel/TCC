from flask import Blueprint
from ..service import github_pull_request_extrator_service as service
from ..repository import github_pull_request_repository as repository
from ..serializer import GithubPullRequestSchema


bp_github_pull_request = Blueprint('github_pull_request', __name__)

@bp_github_pull_request.route('/github-pull-request/repo/<user>/<repo>', methods=['POST'])
def save_user_repos(user, repo):
    service.save_pulls_by_repo(user, repo)
    return '', 200
