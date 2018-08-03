from flask import Blueprint, render_template, url_for, flash, redirect
from flask_login import current_user, login_required

from heirloom.ui import db
from heirloom.ui.models.organization import Organization
from heirloom.ui.models.user import User
from heirloom.ui.forms.user import UserForm

# ==============================================================================
# user API
# ==============================================================================
# define namespace
bp = Blueprint('user', __name__)

# set default route
@bp.route('/', methods=['GET', 'POST'])
@login_required
def user():
    # check that the current user is an admin
    if current_user.get_role_name() is not 'Admin':
        return redirect(url_for('home.home'))

    # validate form
    form = UserForm()
    form.organization.choices = [(0, "None")] + [(o.id, o.name) for o in Organization.query.order_by('name')]
    if form.validate_on_submit():
        # form is valid, create the new user
        if form.organization.data:
            org = Organization.query.get(form.organization.data)
            user = User(username=form.username.data, email=form.email.data, 
                role=form.role.data, organization=org)
        else:
            user = User(username=form.username.data, email=form.email.data, role=form.role.data)

        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Succesfully created new user", category="success")
        return redirect(url_for('user.user'))

    else:
        # handle an invalid form
        return render_template('user.jinja2', title='Users', form=form, users=User.query.all())

    return render_template('user.jinja2', title='Users', form=form, users=User.query.all())
# ==============================================================================
