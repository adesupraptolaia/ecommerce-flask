from blueprints import db
from flask_restful import fields


class Wishlist(db.Model):
    __tablename__ = "wishlist"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, nullable=False)
    product_name = db.Column(db.String(100), nullable = False)
    product_image = db.Column(db.String(100), nullable = False)
    price = db.Column(db.Integer, nullable=False, default=1)

    response_fields = {
        'id' : fields.Integer,
        'client_id': fields.Integer,
        'product_id': fields.Integer,
        'product_name': fields.String,
        'product_image': fields.String,
        'price': fields.Integer
    }

    def __init__(self, client_id, product_id, product_name, product_image, price):
        self.client_id = client_id
        self.product_id = product_id
        self.product_name = product_name
        self.product_image = product_image
        self.price = price

    def __repr__(self):
        return '<Cart %r>' % self.id
