from flask import Blueprint, render_template

#==============================================================================
# home API 
#==============================================================================
# define namespace
bp = Blueprint('home', __name__)

#set default route
@bp.route('/')
def home():
  return render_template('home.html', title='Heirloom Home', username='USER')
#==============================================================================
