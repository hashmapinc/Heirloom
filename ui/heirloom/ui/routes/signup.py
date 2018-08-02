from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user

from heirloom.ui import db
from heirloom.ui.forms.signup import SignupForm
from heirloom.ui.models.user import User

#==============================================================================
# Signup API
#==============================================================================
# define namespace
bp = Blueprint('signup', __name__)

# set default route
@bp.route('/', methods=['GET', 'POST'])
def signup():
  # if the user is logged in, redirect home
  if current_user.is_authenticated:
    return redirect(url_for('home.home'))

  # validate signup form
  form = SignupForm()
  if form.validate_on_submit():
    # form is valid, create the user
    user = User(username=form.username.data, email=form.email.data, role=form.role.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
    flash('Congratulations, you are now a registered user!')
    return redirect(url_for('login.login'))

  else:
    # handle an invalid form
    return render_template('signup.jinja2', title='Signup', form=form)
#==============================================================================
