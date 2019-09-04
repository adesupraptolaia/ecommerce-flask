from flask import Blueprint
from flask_restful import Resource, Api, reqparse, marshal, inputs
from .model import Products
from sqlalchemy import desc
from blueprints import app, db, internal_required, non_internal_required
from flask_jwt_extended import jwt_required, get_jwt_claims, get_jwt_identity


bp_product = Blueprint('product', __name__)
api = Api(bp_product)


class ProductResource(Resource):
    
    def options(self, id=None):
        return {"status": "oke"}, 200


    # @jwt_required
    # @internal_required
    def get(self, id):  # get by id
        qry = Products.query.get(id)
        if qry is not None:
            return marshal(qry, Products.response_fields), 200, {'Content-Type': 'application/json'}
        return {'status': 'Product Not Found'}, 404, {'Content-Type': 'application/json'}

    @jwt_required
    @internal_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', location='json', required=True)
        parser.add_argument('description', location='json', required=True)
        parser.add_argument('category', location='json', required=True)
        parser.add_argument('image', location='json', required=True)
        parser.add_argument('price', type=int, location='json', required=True)
        parser.add_argument('discount', type=int, location='json', required=True)
        parser.add_argument('stock', type=int, location='json', required=True)
        data = parser.parse_args()

        # set value of price_after_discount
        price_after_discount = 0
        if data['discount'] != 0:
            price_after_discount = (data['price'] * (100 - data['discount']))/100
        else:
            price_after_discount = data['price']
            
        product = Products(
            data['name'], 
            data['description'], 
            data['category'],
            data['image'], 
            data['price'], 
            data['discount'],
            price_after_discount, 
            data['stock']
        )

        db.session.add(product)
        db.session.commit()

        app.logger.debug('DEBUG : %s', product)

        return marshal(product, Products.response_fields), 200, {'Content-Type': 'application/json'}

    @jwt_required
    @internal_required
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', location='json', required=True)
        parser.add_argument('description', location='json', required=True)
        parser.add_argument('category', location='json', required=True)
        parser.add_argument('image', location='json', required=True)
        parser.add_argument('price', type=int, location='json', required=True)
        parser.add_argument('discount', type=int, location='json', required=True)
        parser.add_argument('stock', type=int, location='json', required=True)
        data = parser.parse_args()

        qry = Products.query.get(id)
        if qry is None:
            return {'status': 'Product Not Found'}, 404, {'Content-Type': 'application/json'}

        price_after_discount = 0
        if data['discount'] != 0:
            price_after_discount = (data['price'] *(100 - data['discount']))/100
        else:
            price_after_discount = data['price']

        qry.name = data['name']
        qry.description = data['description']
        qry.category = data['category']
        qry.image = data['image']
        qry.price = data['price']
        qry.discount = data['discount']
        qry.price_after_discount = price_after_discount
        qry.stock = data['stock']
        db.session.commit()

        return marshal(qry, Products.response_fields), 200, {'Content-Type': 'application/json'}


    @jwt_required
    @internal_required
    def delete(self, id):
        qry = Products.query.get(id)
        if qry is None:
            return {'status': 'Product Not Found'}, 404, {'Content-Type': 'application/json'}

        db.session.delete(qry)
        db.session.commit()

        return {'status': 'Product Deleted'}, 200, {'Content-Type': 'application/json'}


class ProductList(Resource):

    def options(self):
        return {"status": "oke"}, 200

    def __init__(self):
        pass

    
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default=1)
        parser.add_argument('rp', type=int, location='args', default=25)
        parser.add_argument('category', type=str, location='args')
        data = parser.parse_args()

        offset = (data['p'] * data['rp']) - data['rp']
        
        qry = Products.query

        if data['category'] is not None:
            qry = qry.filter_by(category=data['category'])

        qry = qry.order_by((Products.id))

        rows = []
        for row in qry.limit(data['rp']).offset(offset).all():
            rows.append(marshal(row, Products.response_fields))
        return rows, 200, {'Content-Type': 'application/json'}


api.add_resource(ProductList, '')
api.add_resource(ProductResource, '', '/<id>')
