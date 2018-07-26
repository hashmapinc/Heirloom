from heirloom.ui import db

# class for structuring an organization 
class Organization(db.Model):
    __tablename__ = "organizations"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    address = db.Column(db.String(120), index=True, unique=True)
    members = db.relationship('User', backref='organization', lazy='dynamic')


    def __repr__(self):
        return '<Organization id={}, name={}, address={}>'.format(
            self.id, self.name, self.address)
