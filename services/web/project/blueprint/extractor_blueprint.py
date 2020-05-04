from flask import Blueprint
from ..service import extractor_service as service

bp_extractor = Blueprint('extractor', __name__)

@bp_extractor.route('/extract/<user>/<steps>', methods=['POST'])
def extract(user, steps):
    service.extract(user, steps)
    return '', 200