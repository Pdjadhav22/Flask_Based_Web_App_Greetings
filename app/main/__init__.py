# Main Blueprint creation
from flask import Blueprint

blueprint = Blueprint('main', __name__)
print('Main blueprint created', blueprint.import_name)

# from . import views, errors


#from . import <some-module> syntax is used in Python to represent relative imports
# . in this statement represents the current package

# Views module , Need to work on to keep in different file
from flask import Flask, redirect, url_for, render_template, session,  flash
from .WForms import nameForm
from ..import db
# from .import main
from ..models import User

#to handle oprerational Errors
from sqlalchemy.exc import OperationalError


# creating home route & view function
@ blueprint.route('/', methods=['GET','POST'])
def index():
    # name = None
    form = nameForm()
    if form.validate_on_submit():
        #To catch operatinal errors
        try:
        # recording each user in database
             user = User.query.filter_by(username=form.name.data).first()
        except OperationalError:
            return render_template('Operational_error.html')
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known']=False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.index')) # .index is namespace of blueprint to endpoints/view functions, so that multiple blueprints can  define vew function without collision


        # # for only Web form understanding - to show Flashed messages
        # old_name = session.get('name')
        # if old_name and old_name!= form.name.data:
        #     flash("Looks like you have changed your name")
        # session['name'] = form.name.data
        # # form.name.data = ''
        # return redirect(url_for('index'))
        
    return render_template('index.html', form=form, name = session.get('name'), known=session.get('known',False))  # Session. get give default None value if key is not present

# Error handling in main blueprint

# from flask import render_template
# from . import main


@blueprint.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# errorhandler - it will be invoked only for errors originated in routes defined by the blueprint
# app_errorhandler - it installs application-wide error handlers
