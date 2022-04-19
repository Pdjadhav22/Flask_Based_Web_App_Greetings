# Application Package Constructor

from flask import Flask
from config import config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

# creating flask extension WO initialising
bootstrap = Bootstrap()

# db object instantiated from the class SQLAlchemy represents the database and provides access to all the functionality of Flask-SQLAlchemy.
db = SQLAlchemy()


# Application Factory Function - 
#1. by this we can create multiple instance of an application
#2. helps in delaying creating application instance, meantime different required configuration can be set, useful for unit testing
def create_app(config_name):
    app = Flask(__name__)

    # app configuration
    app.config.from_object(config[config_name])

    # initializing all application extensions
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)

    # Blueprint registeration with application inside factory function
    from .main import blueprint as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
