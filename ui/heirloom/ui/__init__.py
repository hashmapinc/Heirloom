from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from heirloom.ui.config import Config

#==============================================================================
# App setup
#==============================================================================
# Setup flask
app = Flask(__name__)
app.config.from_object(Config)

# Setup database and db migrate utility
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# setup flask login
login = LoginManager(app)
login.login_view = 'login.login'
#==============================================================================
