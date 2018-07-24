from flask import Flask, Blueprint

from heirloom_ui.config import Config
from heirloom_ui.routes.restplus import restplus_api
from heirloom_ui.routes.login import bp as login_blueprint
from heirloom_ui.routes.home import bp as home_blueprint

#==============================================================================
# App 
#==============================================================================
# Setup flask
app = Flask(__name__)
app.config.from_object(Config)

# register restplus with flask
blueprint = Blueprint('api', __name__)
restplus_api.init_app(blueprint)
app.register_blueprint(blueprint, url_prefix='/api')

# register blueprint modules
app.register_blueprint(login_blueprint) # default route
app.register_blueprint(home_blueprint, url_prefix='/home')

# Run app
if __name__ == '__main__':
  app.jinja_env.auto_reload = True
  app.run(host='0.0.0.0', port=80, debug=True)
#==============================================================================
