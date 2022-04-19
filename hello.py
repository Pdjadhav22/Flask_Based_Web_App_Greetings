# Main Application Script

from flask_migrate import Migrate, upgrade
from app import create_app, db
from app.models import User, Role
import os

# creating application from application instance
app = create_app(os.getenv('FLASK_CONFIG') or 'default')

# instantiate flask migration
migrate = Migrate(app, db)


# flask Shell - Integeration with python shell
@app.shell_context_processor
def make_shell():
    return dict(db=db, User=User, Role=Role)

#Unit Test Launcher command
@app.cli.command()
def test():
    """Run the Unit test"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@app.cli.command()
def deploy():
    """Run deployment tasks."""
    # migrate database to latest revision
    upgrade()

    # create or update user roles
    Role.insert_roles()

    # ensure all users are following themselves
    User.add_self_follows()