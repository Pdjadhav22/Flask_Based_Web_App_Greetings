# Error handling in main blueprint

from flask import render_template
from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# errorhandler - it will be invoked only for errors originated in routes defined by the blueprint
# app_errorhandler - it installs application-wide error handlers
