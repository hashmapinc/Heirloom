from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user

#==============================================================================
# home API 
#==============================================================================
# define namespace
bp = Blueprint('home', __name__)

#set default route
@bp.route('/')
def home():
  # if not signed in, reroute to login
  if not current_user.is_authenticated:
    return redirect(url_for('login.login'))
  
  return render_template('home.html', title='Heirloom Home', username="current_user.")
#==============================================================================
