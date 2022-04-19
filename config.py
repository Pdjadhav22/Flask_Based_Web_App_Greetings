# application configuration

import os


# getting absolute path of current file
basdir = os.path.abspath(os.path.dirname(__file__))
# print(basdir)

class ConfigMan:
    SECRET_KEY= os.environ.get('SECRET_KEY') #or 'Hard to Guess'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basdir+ '\SQLA_practice.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# its a way of constructing an instance of packages for application
    @staticmethod
    def init_app(app):
        pass

# Setting up databases for differet phases of a project lifecycle
class devConfig(ConfigMan):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///'+ os.path.join(basdir+ '\SQLA_practice.db')

class testConfig(ConfigMan):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite://'

class prodConfig(ConfigMan):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///'+ os.path.join(basdir+ '\SQLA_practice_prod.db')

config = {

    'development' : devConfig,
    'testing' : testConfig,
    'production' : prodConfig,
    'heroku': HerokuConfig,
    'default' : devConfig
}

# Heroku configuration for Loggings
class HerokuConfig(prodConfig):
    @classmethod
    def init_app(cls,app):
        prodConfig.init_app(app)

        # log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)