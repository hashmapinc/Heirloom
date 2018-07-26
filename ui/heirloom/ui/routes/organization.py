from flask import Blueprint, render_template, url_for, flash, redirect
from flask_login import current_user, login_required

from heirloom.ui import db
from heirloom.ui.models.organization import Organization
from heirloom.ui.forms.organization import OrganizationForm

# ==============================================================================
# organization API
# ==============================================================================
# define namespace
bp = Blueprint('organization', __name__)

# set default route
@bp.route('/', methods=['GET', 'POST'])
@login_required
def organization():
    # validate form
    form = OrganizationForm()
    if form.validate_on_submit():
        # form is valid, create the organization
        org = Organization(name=form.name.data, address=form.address.data)
        db.session.add(org)
        db.session.commit()
        flash("Succesfully created organization")
        return redirect(url_for('organization.organization'))

    else:
        # handle an invalid form
        return render_template('organization.jinja2', title='Organizations', form=form, organizations=Organization.query.all())
    
    return render_template('organization.jinja2', title='Organizations', form=form, organizations=Organization.query.all())
# ==============================================================================
