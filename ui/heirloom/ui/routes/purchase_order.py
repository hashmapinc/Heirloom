from flask import Blueprint, render_template, url_for, flash, redirect, request, jsonify
from flask_login import current_user, login_required

from heirloom.ui import db
from heirloom.ui.models.organization import Organization
from heirloom.ui.models.user import User
from heirloom.ui.models.purchase_order import PurchaseOrder, order_status_codes as ORDER_STATUS
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
        flash("Succesfully created Purchase Order", category="success")
        return redirect(url_for('purchase_order.purchase_order'))

    else:
        # handle an invalid form
        return render_template('purchase_order.jinja2', title='Purchase Orders', form=form, POs=PurchaseOrder.query.all())

    return render_template('purchase_order.jinja2', title='Purchase Orders', form=form, POs=PurchaseOrder.query.all())


# endpiont for getting purchase order details
@bp.route('/<po_id>', methods=['GET'])
@login_required
def details(po_id):
    # validate the po_id
    po = PurchaseOrder.query.get(po_id)

    if po is None:
        # handle an invalid purchase order ID
        flash("Purchase Order not found", category="error")
        return redirect(url_for('purchase_order.purchase_order'))

    else:
        # handle a valid purchase order ID
        return render_template('po_details/po_details.jinja2', title='Purchase Orders > Details', po=po)


# endpiont for getting all transactions from a purchase order
@bp.route('/<po_id>/transactions', methods=['GET'])
@login_required
def transactions(po_id):
    # validate the po_id
    po = PurchaseOrder.query.get(po_id)

    if po is None:
        # handle an invalid purchase order ID
        return "Purchase Order not found", 400

    else:
        # handle a valid purchase order ID
        transactions = [t.to_dict() for t in po.transactions] # convert to serializable dict list
        return jsonify(transactions), 200


# endpiont for accepting a purchase order
@bp.route('/<po_id>/accept', methods=['GET'])
@login_required
def accept(po_id):
    # check that the current user has the proper role
    if current_user.get_role_name() is not 'Seller':
        flash("You do not have permission to accept this order.", category="warning")
        return redirect(url_for('purchase_order.details', po_id=po_id))

    # validate the po_id
    po = PurchaseOrder.query.get(po_id)

    if po is None:
        # handle an invalid purchase order ID
        flash("Purchase Order not found", category="error")
        return redirect(url_for('purchase_order.purchase_order'))

    if po.selling_organization.id is not current_user.organization.id:
        flash("You do not have permission to accept this order.", category="warning")
        return redirect(url_for('purchase_order.details', po_id=po_id))

    if po.order_status is not ORDER_STATUS['Submitted']:
        flash("You can only accept purchase orders with a status of Submitted", category="warning")
        return redirect(url_for('purchase_order.details', po_id=po_id))
    
    # handle a valid purchase order ID
    po.order_status = ORDER_STATUS['Accepted']
    db.session.add(po)
    db.session.commit()
    flash("Succesfully accepted " + po.title, category="success")
    return redirect(url_for('purchase_order.details', po_id=po.id))


# endpiont for requesting payment for a purchase order
@bp.route('/<po_id>/request_payment', methods=['GET'])
@login_required
def request_payment(po_id):
    # check that the current user has the proper role
    if current_user.get_role_name() is not 'Seller':
        flash("You do not have permission to request payment for this order.", category="warning")
        return redirect(url_for('purchase_order.details', po_id=po.id))

    # validate the po_id
    po = PurchaseOrder.query.get(po_id)

    if po is None:
        # handle an invalid purchase order ID
        flash("Purchase Order not found", category="error")
        return redirect(url_for('purchase_order.purchase_order'))

    if po.selling_organization.id is not current_user.organization.id:
        flash("You do not have permission to accept this order.", category="warning")
        return redirect(url_for('purchase_order.purchase_order'))

    if po.order_status == ORDER_STATUS["Submitted"] or po.order_status == ORDER_STATUS["Declined"]:
        flash("You cannot request payment for an order with status of 'Submitted' or 'Declined'." +
              ORDER_STATUS['Submitted'], category="warning")
        return redirect(url_for('purchase_order.details', po_id=po.id))

    # handle a valid request
    po.order_status = ORDER_STATUS['Finished']
    db.session.add(po)
    db.session.commit()
    flash("Succesfully requested payment for " + po.title, category="success")
    return redirect(url_for('purchase_order.details', po_id=po.id))
# ==============================================================================
