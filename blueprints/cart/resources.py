from flask import Blueprint
from flask_restful import Api, reqparse, Resource, marshal
import json
from .model import Cart
from ..product.model import Products
from ..client.model import Clients
from ..transaction_detail.model import Transaction_detail
from flask_jwt_extended import jwt_required, get_jwt_claims
from blueprints import db, app, internal_required, non_internal_required

bp_cart = Blueprint('cart', __name__)
api = Api(bp_cart)



class CartResource(Resource):

    def options(self, id=None):
        return {"status": "oke"}, 200

    # method to add items to cart
    
    
    @jwt_required
    @non_internal_required
    def delete(self, id):
        
        qry = Cart.query.get(id)
        if qry is None:
            return {'status': 'Product Not Found'}, 404, {'Content-Type': 'application/json'}

        db.session.delete(qry)
        db.session.commit()

        return {'status': 'Product Deleted'}, 200, {'Content-Type': 'application/json'}


    @jwt_required
    @non_internal_required
    def get(self):
        claims = get_jwt_claims()
        client_id = claims['id']
        qry = Cart.query.filter_by(client_id = int(client_id)).all()

        cart_items = []
        for item in qry:
            cart_items.append(marshal(item, Cart.response_fields))
        return cart_items, 200, {'Content-Type': 'application/json'}

    @jwt_required
    @non_internal_required
    def post(self):
        parser = reqparse.RequestParser()
        claims = get_jwt_claims()

        client_id = claims['id']

        parser.add_argument('product_id', location='json', required=True)
        parser.add_argument('qty', location='json', default=1)

        data = parser.parse_args()
        product_qry = Products.query.get(int(data['product_id']))

        # get the product price from product table
        product_price = product_qry.price_after_discount * int(data['qty'])
        
        # if demand > stock
        if  int(data['qty']) > int(product_qry.stock):
            return {"status": "Stock not enough"}, 400

        # if product has been in cart
        cart_qry = Cart.query.filter_by(product_id=int(data['product_id']))
        cart_qry = cart_qry.filter_by(client_id=int(client_id)).first()
        if cart_qry is None:
            
            #get the product name from product table
            product_name = Products.query.get(int(data['product_id'])).name


            #get the product image from product table
            product_image = Products.query.get(int(data['product_id'])).image

            # adding product to carts
            cart = Cart(client_id, data['product_id'], product_name, product_image, data['qty'], product_price)

            db.session.add(cart)
            db.session.commit()

            return marshal(cart, Cart.response_fields), 200, {'Content-Type': 'application/json'}
        else:
            cart_qry.qty = data['qty']
            cart_qry.price = product_price
            db.session.commit()

            return marshal(cart_qry, Cart.response_fields), 200, {'Content-Type': 'application/json'}

    


api.add_resource(CartResource, '', '/<id>')


        
