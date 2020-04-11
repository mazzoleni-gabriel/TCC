from flask import Blueprint
from ..service import github_repository_extrator_service as service
from ..repository import github_repository_repository as repository
from ..serializer import GithubRepositorySchema


bp_github_repository = Blueprint('github_repository', __name__)

@bp_github_repository.route('/github-repository', methods=['GET'])
def list_all():
    schema = GithubRepositorySchema(many = True)
    result = repository.list_all()
    return schema.jsonify(result), 200

@bp_github_repository.route('/github-repository/<_id>', methods=['GET'])
def get(_id):
    schema = GithubRepositorySchema()
    result = repository.get_by_id(_id)
    return schema.jsonify(result), 200

@bp_github_repository.route('/github-repository/user/<login>', methods=['POST'])
def save_user_repos(login):
    service.save_repos_by_user(login)
    return '', 200
