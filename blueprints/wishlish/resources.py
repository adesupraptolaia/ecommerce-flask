from flask import Blueprint
from flask_restful import Api, reqparse, Resource, marshal
import json
from .model import Wishlist
from ..product.model import Products
from ..client.model import Clients
from flask_jwt_extended import jwt_required, get_jwt_claims
from blueprints import db, app, internal_required, non_internal_required

bp_wishlist = Blueprint('wishlist', __name__)
api = Api(bp_wishlist)

#######################
# Using flask-restful
#######################

class WishlistResource(Resource):

    def options(self, id=None):
        return {"status": "oke"}
    
    @jwt_required
    @non_internal_required
    def delete(self, id):
        
        qry = Wishlist.query.get(id)
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
        qry = Wishlist.query.filter_by(client_id = int(client_id)).all()

        wishlist_items = []
        for item in qry:
            wishlist_items.append(marshal(item, Wishlist.response_fields))
        return wishlist_items, 200, {'Content-Type': 'application/json'}

    @jwt_required
    @non_internal_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('product_id', location='json', required=True)
        data = parser.parse_args()

        claims = get_jwt_claims()
        client_id = claims['id']
        


        # if product has been in wishlist
        wishlist_qry = Wishlist.query.filter_by(product_id=int(data['product_id']))
        wishlist_qry = wishlist_qry.filter_by(client_id=int(client_id)).first()
        if wishlist_qry is None:
            
            #get the product name from product table
            product_name = Products.query.get(int(data['product_id'])).name

            # price after dicount
            product_price = Products.query.get(int(data['product_id'])).price_after_discount

            #get the product image from product table
            product_image = Products.query.get(int(data['product_id'])).image

            # adding product to carts
            wishlist = Wishlist(client_id, data['product_id'], product_name, product_image, product_price)

            db.session.add(wishlist)
            db.session.commit()

            return marshal(wishlist, Wishlist.response_fields), 200, {'Content-Type': 'application/json'}
        else:
            return {"status": "barang sudah ada"}, 200, {'Content-Type': 'application/json'}

    


api.add_resource(WishlistResource, '', '/<id>')


        
