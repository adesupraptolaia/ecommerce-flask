from flask import Blueprint
from flask_restful import Resource, Api, reqparse, marshal, inputs
from .model import Transactions
from ..product.model import Products
from ..client.model import Clients
from ..cart.model import Cart
from ..transaction_detail.model import Transaction_detail
from sqlalchemy import desc
from blueprints import app, db, internal_required, non_internal_required
from flask_jwt_extended import jwt_required, get_jwt_claims

bp_transaction = Blueprint('transaction', __name__)
api = Api(bp_transaction)


class TransactionResource(Resource):

    def __init__(self):
        pass

    def options(self, id=None):
        return {"status": "oke"}, 200

    @jwt_required
    @non_internal_required
    def get(self, id):  # get by id
        qry = Transactions.query.get(id)
        if qry is not None:
            return marshal(qry, Transactions.response_fields), 200, {'Content-Type': 'application/json'}
        return {'status': 'transaction_detail Not Found'}, 404, {'Content-Type': 'application/json'}


    @jwt_required
    @non_internal_required
    def post(self):
        claims = get_jwt_claims()
        client_id = claims['id']

        transaction = Transactions(client_id)
        db.session.add(transaction)
        db.session.commit()

        transaction_id = transaction.id

        cart_qry = Cart.query.filter_by(client_id = int(client_id)).all()

        # check if there is product's stock not enough
        for item in cart_qry:
            product_qry = Products.query.get(item.product_id)
            if int(item.qty) > int(product_qry.stock):
                return {"status" : "Habis"}

        # continue if all stock enoungh
        for item in cart_qry:
            product_qry = Products.query.get(item.product_id)
            
            trans_detail = Transaction_detail(transaction_id, client_id, item.product_id, item.product_name, item.qty, item.price)

            # to update transaction price
            transaction.total_price += item.price
            # to decrease the stock of the product
            product_qry.stock -= item.qty
            db.session.commit()

            # adding into trans_detail table
            db.session.add(trans_detail)
            db.session.commit()

            # delete the items in cart database so that when user make more transaction, the old ones will not be included
            db.session.delete(item)
            db.session.commit()

        app.logger.debug('DEBUG : %s', transaction)

        return marshal(transaction, Transactions.response_fields), 200, {'Content-Type': 'application/json'}

    


class TransactionList(Resource):

    def __init__(self):
        pass

    def options(self):
        return {"status": "oke"}, 200
        
    @jwt_required
    @non_internal_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default=1)
        parser.add_argument('rp', type=int, location='args', default=25)
        # parser.add_argument('client_id', type=int, location='json')
        data = parser.parse_args()

        offset = (data['p'] * data['rp']) - data['rp']

        claims = get_jwt_claims()
        qry = Transactions.query.filter_by(client_id=claims['id'])

        rows = []
        for row in qry.limit(data['rp']).offset(offset).all():
            rows.append(marshal(row, Transactions.response_fields))
        return rows, 200, {'Content-Type': 'application/json'}


class TransactionAdminList(Resource):

    def __init__(self):
        pass

    def options(self):
        return {"status": "oke"}, 200
        
    @jwt_required
    @internal_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default=1)
        parser.add_argument('rp', type=int, location='args', default=25)
        parser.add_argument('client_id', type=int, location='args')
        data = parser.parse_args()

        offset = (data['p'] * data['rp']) - data['rp']


        qry = Transactions.query

        if data['client_id'] is not None:
            qry = qry.filter_by(client_id=data['client_id'])

        rows = []
        for row in qry.limit(data['rp']).offset(offset).all():
            rows.append(marshal(row, Transactions.response_fields))
        return rows, 200, {'Content-Type': 'application/json'}

api.add_resource(TransactionList, '')
api.add_resource(TransactionAdminList, '/admin')
api.add_resource(TransactionResource, '', '/<id>')
