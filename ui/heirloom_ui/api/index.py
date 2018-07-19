from flask import Blueprint, render_template

from heirloom_ui.api.restplus import restplus_api

#==============================================================================
# Models API 
#==============================================================================
# define namespace
bp = Blueprint('heirloom_ui', __name__)

#set default route
@bp.route('/')
def index():
  return render_template('index.html')

#==============================================================================
