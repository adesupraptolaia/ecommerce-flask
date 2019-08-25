from blueprints import db
from flask_restful import fields
from datetime import datetime

# BOOKS CLASS


class Transactions(db.Model):
    __tablename__ = "transaction"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Integer, nullable=False, default=0)
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.now)

    response_fields = {
        'id': fields.Integer,
        'client_id': fields.Integer,
        'total_price': fields.Integer,
        'createdAt': fields.DateTime
    }

    def __init__(self, client_id,total_price=0):
        self.client_id = client_id
        self.total_price = total_price

    def __repr__(self):
        return '<Transaction %r>' % self.id
