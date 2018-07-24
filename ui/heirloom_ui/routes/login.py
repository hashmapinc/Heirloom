from flask import Blueprint, render_template, flash, redirect
from heirloom_ui.forms.login import LoginForm

#==============================================================================
# Login API 
#==============================================================================
# define namespace
bp = Blueprint('login', __name__)

#set default route
@bp.route('/', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    flash('Login requested for user {}, remember_me={}'.format(
      form.username.data, form.remember_me.data))
    return redirect('/home')
  return render_template('login.html', title='Heirloom Login', form=form)
#==============================================================================
