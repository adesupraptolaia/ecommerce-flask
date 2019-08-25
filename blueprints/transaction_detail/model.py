from blueprints import db
from flask_restful import fields
from datetime import datetime

# BOOKS CLASS


class Transaction_detail(db.Model):
    __tablename__ = "transaction_detail"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    transaction_id = db.Column(db.Integer, nullable = False)
    client_id = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, nullable=False)    
    product_name = db.Column(db.String(250), nullable = False)
    qty = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now)

    response_fields = {
        'id': fields.Integer,
        'transaction_id': fields.Integer,
        'client_id': fields.Integer,
        'product_id': fields.Integer,
        'product_name': fields.String,
        'qty': fields.Integer,
        'total_price': fields.Integer,
        'date': fields.DateTime
    }

    def __init__(self, transaction_id, client_id, product_id, product_name, qty, total_price):
        self.transaction_id = transaction_id
        self.client_id = client_id
        self.product_id = product_id
        self.product_name = product_name
        self.qty = qty
        self.total_price = total_price

    def __repr__(self):
        return '<Transaction_detail %r>' % self.id
