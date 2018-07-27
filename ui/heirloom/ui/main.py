from heirloom.ui import app, db

# import models
from heirloom.ui.models.user import User
from heirloom.ui.models.organization import Organization
from heirloom.ui.models.purchase_order import PurchaseOrder

# import blueprints
from heirloom.ui.routes.login import bp as login_blueprint
from heirloom.ui.routes.home import bp as home_blueprint
from heirloom.ui.routes.signup import bp as signup_blueprint
from heirloom.ui.routes.organization import bp as org_blueprint
from heirloom.ui.routes.user import bp as user_blueprint

#==============================================================================
# Main 
#==============================================================================
db.create_all()

# register blueprint modules
app.register_blueprint(login_blueprint) # default route
app.register_blueprint(home_blueprint, url_prefix='/home')
app.register_blueprint(signup_blueprint, url_prefix='/signup')
app.register_blueprint(org_blueprint, url_prefix='/org')
app.register_blueprint(user_blueprint, url_prefix='/user')

# Run app
if __name__ == '__main__':
  app.jinja_env.auto_reload = True
  app.run(host='0.0.0.0', port=80, debug=True)
#==============================================================================
