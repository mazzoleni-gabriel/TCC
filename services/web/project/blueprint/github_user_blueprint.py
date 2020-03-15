from flask import Blueprint
from ..service import github_extractor_service
from ..repository import github_user_repository as repository
from ..serializer import GithubUserSchema


bp_github_user = Blueprint('github_user', __name__)

@bp_github_user.route('/github-user', methods=['GET'])
def list_all():
    schema = GithubUserSchema(many = True)
    result = repository.list_all()
    return schema.jsonify(result), 200

@bp_github_user.route('/github-user/<login>', methods=['GET'])
def get(login):
    schema = GithubUserSchema()
    result = repository.get_by_login(login)
    return schema.jsonify(result), 200

@bp_github_user.route('/github-user/<login>', methods=['POST'])
def save(login):
    schema = GithubUserSchema()
    github_user = github_extractor_service.get_user(login)
    return schema.jsonify(repository.save(github_user)), 200