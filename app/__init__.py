from flask import Flask
import os

ROUTE = "db/users.json"


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    if not os.path.exists(ROUTE):
        with open(ROUTE, "w") as f:
            f.close()

    with app.app_context():
        pass

    return app