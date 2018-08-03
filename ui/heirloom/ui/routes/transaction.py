from flask import Blueprint, render_template, url_for, flash, redirect
from flask_login import current_user, login_required

from heirloom.ui import db
from heirloom.ui.models.user import User
from heirloom.ui.models.transaction import Transaction
from heirloom.ui.models.purchase_order import PurchaseOrder, order_status_codes as ORDER_STATUS
from heirloom.ui.forms.transaction import TransactionForm

# ==============================================================================
# transaction API
# ==============================================================================
# define namespace
bp = Blueprint('transaction', __name__)

# set default route
@bp.route('/', methods=['GET', 'POST'])
@login_required
def transaction():
    # create form
    form = TransactionForm()
    purchase_orders = PurchaseOrder.query.order_by('title')
    form.purchase_order_id.choices = [(0, "Purchase Order")] + [(po.id, po.title) for po in purchase_orders]

    # validate form
    if form.validate_on_submit():
        # form is valid, add transaction
        po = PurchaseOrder.query.get(form.purchase_order_id.data)
        transaction = Transaction(
            type=form.type.data, 
            notes=form.notes.data, 
            author=current_user, 
            value=form.value.data,
            purchase_order=po)
        db.session.add(transaction)
        db.session.commit()
        flash("Succesfully added transaction", category="success")
        return redirect(url_for('transaction.transaction'))

    else:
        # handle an invalid form
        return render_template('transaction.jinja2', title='Transactions', form=form, transactions=Transaction.query.all())

    return render_template('transaction.jinja2', title='Transactions', form=form, transactions=Transaction.query.all())


# endpiont for getting transaction details
@bp.route('/<transaction_id>', methods=['GET'])
@login_required
def details(transaction_id):
    # validate the transaction_id
    txn = Transaction.query.get(transaction_id)

    if txn is None:
        # handle an invalid transaction ID
        flash("Transaction not found", category="error")
        return redirect(url_for('transaction.transaction'))

    else:
        # handle a valid purchase order ID
        return render_template('transaction_details.jinja2', title='Transactions > Details', txn=txn)
# ==============================================================================
