from blueprints import db
from flask_restful import fields

# BOOKS CLASS


class Products(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(30), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    discount = db.Column(db.Integer, nullable=False)
    price_after_discount = db.Column(db.Integer, nullable=False)    
    stock = db.Column(db.Integer, nullable=False)

    response_fields = {
        'id': fields.Integer,
        'name': fields.String,
        'description': fields.String,
        'category': fields.String,
        'image': fields.String,
        'price': fields.Integer,
        'discount': fields.Integer,
        'price_after_discount': fields.Integer,
        'stock': fields.Integer
    }

    def __init__(self, name, description, category, image, price, discount, price_after_discount, stock):
        self.name = name
        self.description = description
        self.category = category
        self.image = image
        self.price = price
        self.discount = discount
        self.price_after_discount = price_after_discount
        self.stock = stock

    def __repr__(self):
        return '<Product %r>' % self.id
