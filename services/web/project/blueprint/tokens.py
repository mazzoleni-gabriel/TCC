from flask import Blueprint, request
from ..repository import token_repository as repository
from ..serializer import TokenSchema
from ..service import reset_token_service


bp_tokens = Blueprint('tokens', __name__)

@bp_tokens.route('/token/list', methods=['GET'])
def list_all():
    schema = TokenSchema(many=True)
    result = repository.list_all()
    return schema.jsonify(result), 200

@bp_tokens.route('/token/<_id>', methods=['GET'])
def get(_id):
    schema = TokenSchema()
    result = repository.get_by_id(_id)
    return schema.jsonify(result), 200

@bp_tokens.route('/token/available', methods=['GET'])
def get_available():
    schema = TokenSchema()
    result = reset_token_service.get_available_token()
    return schema.jsonify(result), 200

@bp_tokens.route('/token/', methods=['POST'])
def save():
    schema = TokenSchema()
    token = schema.load(request.json)

    result = repository.save(token)

    return schema.jsonify(result), 201

@bp_tokens.route('/token/<_id>', methods=['PUT'])
def update(_id):
    schema = TokenSchema()
    result  = repository.update(_id, request.json)

    return schema.jsonify(result), 200

@bp_tokens.route('/token/<_id>', methods=['DELETE'])
def delete(_id):
    repository.delete(_id)

    return '', 200
