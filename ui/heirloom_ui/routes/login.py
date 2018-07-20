from flask import Blueprint, render_template
from heirloom_ui.forms.login import LoginForm

#==============================================================================
# Login API 
#==============================================================================
# define namespace
bp = Blueprint('heirloom_ui', __name__)

#set default route
@bp.route('/login')
def index():
  form = LoginForm()
  return render_template('login.html', title='Heirloom Login', form=form)

#==============================================================================
