from flask import Blueprint, render_template, url_for, flash, redirect
from flask_login import current_user, login_required

from heirloom.ui import db
from heirloom.ui.models.organization import Organization
from heirloom.ui.models.user import User
from heirloom.ui.models.purchase_order import PurchaseOrder
from heirloom.ui.forms.purchase_order import PurchaseOrderForm

# ==============================================================================
# purchase order API
# ==============================================================================
# define namespace
bp = Blueprint('purchase_order', __name__)

# set default route
@bp.route('/', methods=['GET', 'POST'])
@login_required
def purchase_order():
    # validate form
    form = PurchaseOrderForm()
    form.selling_organization.choices = [(0, "Vendor")] + [(o.id, o.name) for o in Organization.query.order_by('name')]
    if form.validate_on_submit():
        # form is valid, create the purchase order
        po = PurchaseOrder(
            title=form.title.data, 
            order_details=form.order_details.data, 
            author=current_user, 
            buying_organization=current_user.organization, 
            selling_organization=Organization.query.get(form.selling_organization.data))
        db.session.add(po)
        db.session.commit()
        flash("Succesfully created Purchase Order")
        return redirect(url_for('purchase_order.purchase_order'))

    else:
        # handle an invalid form
        return render_template('purchase_order.jinja2', form=form, POs=PurchaseOrder.query.all())

    return render_template('purchase_order.jinja2', form=form, POs=PurchaseOrder.query.all())
# ==============================================================================
