from flask_marshmallow import Marshmallow
from .model import Token

ma = Marshmallow()

def configure(app):
    ma.init_app(app)

class TokenSchema(ma.ModelSchema):
    class Meta:
        model = Token

