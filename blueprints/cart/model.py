from blueprints import db
from flask_restful import fields


class Cart(db.Model):
    __tablename__ = "cart"
    cart_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, nullable=False)
    product_name = db.Column(db.String(100), nullable = False)
    product_image = db.Column(db.String(100), nullable = False)
    qty = db.Column(db.Integer, nullable=False, default=1)
    price = db.Column(db.Integer, nullable=False, default=1)

    response_fields = {
        'cart_id' : fields.Integer,
        'client_id': fields.Integer,
        'product_id': fields.Integer,
        'product_name': fields.String,
        'product_image': fields.String,
        'qty': fields.Integer,
        'price': fields.Integer
    }

    def __init__(self, client_id, product_id, product_name, product_image, qty, price):
        self.client_id = client_id
        self.product_id = product_id
        self.product_name = product_name
        self.product_image = product_image
        self.qty = qty
        self.price = price

    def __repr__(self):
        return '<Cart %r>' % self.cart_id
