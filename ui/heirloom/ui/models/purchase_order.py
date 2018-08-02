from datetime import datetime

from heirloom.ui import db


order_status_codes = {
    '':             0,
    'Submitted':    1,
    'Accepted':     2,
    'In Progress':  3,
    'Declined':     4,
    'Finished':     5
}
order_statuses = [(order_status_codes[key], key) for key in order_status_codes]


payment_status_codes = {
    '':         0,
    'Unpaid':   1,
    'Paid':     2
}
payment_statuses = [(payment_status_codes[key], key) for key in payment_status_codes]

# class for structuring a purchase order
class PurchaseOrder(db.Model):
    __tablename__ = "purchase_orders"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    order_details = db.Column(db.String()) # TODO: currently this is a string, but it should be it's own data model
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    buying_organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id'), index=True)
    selling_organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id'), index=True)
    order_status = db.Column(db.Integer, nullable=False, default=1)
    payment_status = db.Column(db.Integer, nullable=False, default=1)

    buying_organization = db.relationship(
        'Organization', foreign_keys='PurchaseOrder.buying_organization_id')
    selling_organization = db.relationship(
        'Organization', foreign_keys='PurchaseOrder.selling_organization_id')

    def get_order_status_name(self):
        try:
            return order_statuses[self.order_status][1]
        except:
            return ''

    def get_payment_status_name(self):
        try:
            return payment_statuses[self.payment_status][1]
        except:
            return ''

    def __repr__(self):
        return '<PurchaseOrder id={}, title={}, timestamp={}, order_details={}, author={}, buying_organization={}, selling_organization={}, order_status={}, payment_status={}>'.format(
            self.id, self.title, self.timestamp, self.order_details, self.author, self.buying_organization, self.selling_organization, self.get_order_status_name(), self.get_payment_status_name())
