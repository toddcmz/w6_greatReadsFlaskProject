from flask import Flask

app = Flask(__name__)

from app.blueprints.auth import bp as auth_bp
app.register_blueprint(auth_bp)
from app.blueprints.main import bp as main_bp
app.register_blueprint(main_bp)
from app.blueprints.mybooks import bp as mybooks_bp
app.register_blueprint(mybooks_bp)