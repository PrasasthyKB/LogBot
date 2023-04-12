import os
from flask import Flask, app, Blueprint
from flask_restful import Api
# from flask_restx import Api
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
# from flask_marshmallow import Marshmallow

# routes
from routes import create_routes

default_config = { 'MONGODB_SETTINGS': {
    'db': 'logbotdatabase',
    'host': 'mongodb://128.214.254.176/logbotdatabase',
    'port': 9005   
}, 'JWT_SECRET_KEY': 'changeThisKeyFirst'}

def get_flask_app(config: dict = None) -> app.Flask:
    """
    Initializes Flask app with given configuration.
    :param config: Configuration dictionary
    :return: app
    """
    # init flask
    flask_app = Flask(__name__)
    blue_print = Blueprint('api', __name__, url_prefix='/api')
    flask_app.register_blueprint(blue_print)

    # configure app
    config = default_config if config is None else config
    flask_app.config.update(default_config)
   
    if 'JWT_SECRET_KEY' in os.environ:
        flask_app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']

    # init api and routes
    api = Api(app=flask_app)
    create_routes(api=api)

    # init mongoengine
    mongo_db = MongoEngine()
    mongo_db.init_app(flask_app)
    
    # init marshmallow
    # marshmallow = Marshmallow()
    # marshmallow.init_app(flask_app)

    # init jwt manager
    jwt = JWTManager(app=flask_app)
    return flask_app


if __name__ == '__main__':
    # Main entry point when run in stand-alone mode.
    app = get_flask_app()
    app.run(debug=True)