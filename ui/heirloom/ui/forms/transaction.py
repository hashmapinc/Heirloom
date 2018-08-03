from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, ValidationError

from heirloom.ui.models.purchase_order import PurchaseOrder

# form for creating new transactions
class TransactionForm(FlaskForm):
    type = StringField('Type', validators=[DataRequired()])
    value = StringField('Value', validators=[DataRequired()])
    notes = TextAreaField('Notes')
    purchase_order_id = SelectField(u'Purchase Order', default=0, coerce=int, validators=[DataRequired()])
    submit = SubmitField('Add')

    def validate_purchase_order_id(self, purchase_order_id):
        if purchase_order_id.data and purchase_order_id.data > 0:
            po = PurchaseOrder.query.get(purchase_order_id.data)
            if po is None:
                raise ValidationError('Could not find chosen purchase order.')
        else:
            raise ValidationError('Invalid purchase order.')
