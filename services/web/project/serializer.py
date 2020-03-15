from flask_marshmallow import Marshmallow
from .model import Token, Github_user

ma = Marshmallow()

def configure(app):
    ma.init_app(app)

class TokenSchema(ma.ModelSchema):
    class Meta:
        model = Token

class GithubUserSchema(ma.ModelSchema):
    class Meta:
        model = Github_user
