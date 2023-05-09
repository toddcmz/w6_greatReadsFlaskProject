from flask import Blueprint

bp = Blueprint('mybooks', __name__, url_prefix='/mybooks')

from app.blueprints.mybooks import routes