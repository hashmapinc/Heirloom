from datetime import datetime

from heirloom.ui import db

# class for structuring a transaction
class Transaction(db.Model):
    __tablename__ = "transactions"

    id =                db.Column(db.Integer, primary_key=True)
    timestamp =         db.Column(db.DateTime, index=True, default=datetime.utcnow, nullable=False)
    notes =             db.Column(db.String())
    type =              db.Column(db.String(), nullable=False)
    value =             db.Column(db.String(), nullable=False)
    author_id =         db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    purchase_order_id = db.Column(db.Integer, db.ForeignKey('purchase_orders.id'), index=True, nullable=False)

    def __repr__(self):
        return '<Transaction id={}, timestamp={}, notes={}, author={}, type={}, value={}, purchase_order={}>'.format(
            self.id, self.timestamp, self.notes, self.author, self.type, self.value, self.purchase_order())
