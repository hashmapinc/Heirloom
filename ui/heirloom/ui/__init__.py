from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from heirloom.ui.config import Config

#==============================================================================
# App setup
#==============================================================================
# Setup flask
app = Flask(__name__)
app.config.from_object(Config)

# Setup database
db = SQLAlchemy(app)

# setup flask login
login = LoginManager(app)
#==============================================================================
