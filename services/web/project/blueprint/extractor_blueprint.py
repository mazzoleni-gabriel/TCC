from flask import Blueprint
from ..service import extractor_service as service
import time


bp_extractor = Blueprint('extractor', __name__)

@bp_extractor.route('/extract/<user>/<steps>', methods=['POST'])
def extract(user, steps):
    start_time = time.time()
    service.extract(user, steps)
    print("--- extractor total time time:  %s seconds ---" % (time.time() - start_time))
    return '', 200