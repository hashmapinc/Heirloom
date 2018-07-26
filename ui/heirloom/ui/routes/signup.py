from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user

from heirloom.ui.forms.signup import SignupForm
from heirloom.ui.models.user import User

#==============================================================================
# Signup API
#==============================================================================
# define namespace
bp = Blueprint('signup', __name__)

# set login route
@bp.route('/', methods=['GET', 'POST'])
def signup():
  # if the user is logged in, redirect home
  if current_user.is_authenticated:
    return redirect(url_for('home.home'))

  # validate login form
  form = SignupForm()
  if form.validate_on_submit():
    # form is valid, get user
    print("valid form")

  else:
    # handle an invalid form
    return render_template('signup.html', title='Heirloom Signup', form=form)
#==============================================================================
