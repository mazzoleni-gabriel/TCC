from flask import Flask, jsonify
from .model import configure as config_db
from .serializer import configure as config_ma


def create_app():
    app = Flask(__name__)
    app.config.from_object("project.config.Config")

    config_db(app)
    config_ma(app)

    from .blueprint.token_blueprint import bp_token
    from .blueprint.github_user_blueprint import bp_github_user
    app.register_blueprint(bp_token)
    app.register_blueprint(bp_github_user)

    return app

app = create_app()

@app.route("/status")
def hello_world():
    return jsonify(status="OK")
