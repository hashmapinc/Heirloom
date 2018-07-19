from flask import Flask, Blueprint

from heirloom_ui.api.restplus import restplus_api
from heirloom_ui.api.index import bp as index_blueprint

#==============================================================================
# App 
#==============================================================================
# Setup flask
app = Flask(__name__)

# register restplus with flask
blueprint = Blueprint('ui', __name__)
restplus_api.init_app(blueprint)
app.register_blueprint(blueprint, url_prefix='/api')

# register index blueprint
app.register_blueprint(index_blueprint)

# Run app
if __name__ == '__main__':
  app.jinja_env.auto_reload = True
  app.run(host='0.0.0.0', port=80, debug=False)
#==============================================================================