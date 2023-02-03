import os
from flask import Flask

ROUTE = "app/db/users.json"


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = "super secreto"

    if not os.path.exists(ROUTE):
        with open(ROUTE, "w") as f:
            f.close()

    with app.app_context():

        from . import auth
        app.register_blueprint(auth.bp_auth)

        from . import home
        app.register_blueprint(home.bp_menu)


    return app