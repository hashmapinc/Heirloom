from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, ValidationError

from heirloom.ui.models.organization import Organization

# form for creating new purchase orders
class PurchaseOrderForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    order_details = TextAreaField('Order Details', validators=[DataRequired()])
    selling_organization = SelectField(u'Vendor', default=0, coerce=int, validators=[DataRequired()])
    submit = SubmitField('Create')

    def validate_selling_organization(self, vendor):
        if vendor.data and vendor.data > 0:
            org = Organization.query.get(vendor.data)
            if org is None:
                raise ValidationError('Could not find chosen vendor.')
        else:
            raise ValidationError('Invalid vendor.')
