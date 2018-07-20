from flask import Flask, Blueprint

from heirloom_ui.config import Config
from heirloom_ui.routes.restplus import restplus_api
from heirloom_ui.routes.login import bp as login_blueprint

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

# register login blueprint
app.register_blueprint(login_blueprint)

# Run app
if __name__ == '__main__':
  app.jinja_env.auto_reload = True
  app.run(host='0.0.0.0', port=80, debug=True)
#==============================================================================
