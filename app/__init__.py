from flask import Flask
from config import Config
from flask_migrate import Migrate
from app.models import db, User
from flask_login import LoginManager
import pandas as pd

app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
#app.register_blueprint(api)

db.init_app(app)
migrate = Migrate(app,db)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

login_manager.login_view='login_page'

from . import routes, models

    