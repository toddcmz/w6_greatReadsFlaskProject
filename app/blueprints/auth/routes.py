from flask import render_template, flash, redirect, url_for
from . import bp
from app.forms import SignupForm
from app.models import User
from app import db

@bp.route('/signin')
def signin():
    return render_template('signin.jinja', title='Sign In')

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
            username = form.username.data
            email = form.email.data
            checkUser = User.query.filter_by(username=username).first()
            checkEmail = User.query.filter_by(email=email).first()
            if not checkUser and not checkEmail:
                thisUser = User(username=username, email=email, password=form.password.data)
                thisUser.commit()
                flash(f"Username '{username}' submitted a sign up request")
                return redirect(url_for('main.home'))
            elif checkUser:
                flash(f'{username} already taken, try again')
            else:
                flash(f'{email} already taken, try again')
    return render_template('signup.jinja', title='Sign Up', form=form)