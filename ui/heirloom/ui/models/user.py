from heirloom.ui.app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.Integer)

    def __repr__(self):
        return '<User id={}, username={}, email={}, role={}>'.format(
            self.id, self.username, self.email, self.role)
