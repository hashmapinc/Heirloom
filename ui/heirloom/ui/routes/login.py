from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user

from heirloom.ui.forms.login import LoginForm
from heirloom.ui.models.user import User

#==============================================================================
# Login API 
#==============================================================================
# define namespace
bp = Blueprint('login', __name__)

# set default route
@bp.route('/')
def index():
  if current_user.is_authenticated:
    return redirect(url_for('home.home'))
  else:
    return redirect(url_for('login.login'))

# set login route
@bp.route('/login', methods=['GET', 'POST'])
def login():
  # if the user is logged in, redirect home
  if current_user.is_authenticated:
    return redirect(url_for('home.home'))
  
  # validate login form
  form = LoginForm()
  if form.validate_on_submit():
    # form is valid, get user
    user = User.query.filter_by(username=form.username.data).first()

    # check user exists and password is correct
    if user is None or not user.check_password(form.password.data):
      # user is invalid
      flash('Invalid username or password')
      return render_template('login.html', title='Heirloom Login', form=form)
    
    # user is valid. Login and redirect
    login_user(user, remember=form.remember_me.data)
    return redirect(url_for('home.home'))
  
  # handle an invalid form
  return render_template('login.html', title='Heirloom Login', form=form)

# set logout route
@bp.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('login.login'))
#==============================================================================
