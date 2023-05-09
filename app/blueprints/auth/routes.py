from flask import render_template
from . import bp

@bp.route('/signin')
def signin():
    return render_template('signin.jinja', title='Sign In')

@bp.route('/signup')
def signup():
    return render_template('signup.jinja', title='Sign Up')