from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
import phonenumbers

# form for creating new organizations
class OrganizationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    address = StringField('Address')
    phone = StringField('Phone')
    submit = SubmitField('Create')

    def validate_phone(self, phone):
        if phone.data:
            if len(phone.data) > 16:
                raise ValidationError('Invalid phone number.')
            try:
                input_number = phonenumbers.parse(phone.data)
                if not (phonenumbers.is_valid_number(input_number)):
                    raise ValidationError('Invalid phone number.')
            except:
                try:
                    input_number = phonenumbers.parse("+1"+phone.data)
                    if not (phonenumbers.is_valid_number(input_number)):
                        raise ValidationError('Invalid phone number.')
                except:
                    raise ValidationError('Invalid phone number.')
