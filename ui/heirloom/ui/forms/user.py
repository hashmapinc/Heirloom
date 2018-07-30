from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError, DataRequired, Email, EqualTo

from heirloom.ui.models.user import User, roles
from heirloom.ui.models.organization import Organization

# form used by admins to provision users
class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    organization = SelectField(u'Organization', default=0, coerce=int)
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[
                              DataRequired(), EqualTo('password')])
    role = SelectField(u'User Role', choices=roles,
                       default=0, validators=[DataRequired()])
    submit = SubmitField('Create')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_organization(self, org_id):
        if org_id.data and org_id.data > 0:
            org = Organization.query.get(org_id.data)
            if org is None:
                raise ValidationError('Could not find chosen organization!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
