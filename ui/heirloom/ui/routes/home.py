from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required

#==============================================================================
# home API 
#==============================================================================
# define namespace
bp = Blueprint('home', __name__)

#set default route
@bp.route('/')
@login_required
def home():
  return render_template('home.jinja2', title='Heirloom Home')
#==============================================================================
