
from flask import Flask, redirect, url_for, render_template, session,  flash
from .WForms import nameForm
from ..import db
from .import main
from ..models import User


# creating home route & view function
@main.route('/', methods=['GET','POST'])
def index():
    # name = None
    form = nameForm()
    if form.validate_on_submit():
        # recording each user in database
        user = User.query.filter_by(username=form.name.data).first()
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