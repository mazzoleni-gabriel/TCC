from flask_marshmallow import Marshmallow
from .model import Token, Github_user, Github_repository, Github_pull_request
ma = Marshmallow()

def configure(app):
    ma.init_app(app)

class TokenSchema(ma.ModelSchema):
    class Meta:
        model = Token

class GithubUserSchema(ma.ModelSchema):
    class Meta:
        model = Github_user

class GithubRepositorySchema(ma.ModelSchema):
    class Meta:
        model = Github_repository

class GithubPullRequestSchema(ma.ModelSchema):
    class Meta:
        model = Github_pull_request
