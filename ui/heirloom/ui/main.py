from heirloom.ui import app, db
from heirloom.ui.routes.login import bp as login_blueprint
from heirloom.ui.routes.home import bp as home_blueprint

#==============================================================================
# Main 
#==============================================================================
db.create_all()

# register blueprint modules
app.register_blueprint(login_blueprint) # default route
app.register_blueprint(home_blueprint, url_prefix='/home')

# Run app
if __name__ == '__main__':
  app.jinja_env.auto_reload = True
  app.run(host='0.0.0.0', port=80, debug=True)
#==============================================================================
