from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from heirloom.ui import db, login

# roles - formatted based on the 'choice' field for the signup select element
roles = [
    ('0', 'Admin'), 
    ('1', 'Buyer'), 
    ('2', 'Seller')
]

# User loader for login extension
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# class for structuring a user 
class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id'))
    role = db.Column(db.Integer, nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_role_name(self):
        try:
            return roles[self.role][1]
        except:
            return ''

    def get_organization_name(self):
        try:
            return self.organization.name
        except:
            return ''

    def __repr__(self):
        return '<User id={}, username={}, email={}, role={}, organization={}>'.format(
            self.id, self.username, self.email, self.role, self.organization.name)
