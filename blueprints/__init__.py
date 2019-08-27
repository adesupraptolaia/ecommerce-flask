from flask import Flask, request
import json
# Import yang dibutuhkan untuk database
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_jwt_extended import JWTManager, verify_jwt_in_request, get_jwt_claims
from datetime import timedelta
from functools import wraps
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
###################################
# JWT
###################################

# Bisa bebas
app.config['JWT_SECRET_KEY'] = 'zENpazwq97E5BqkFUcAdc9ssMqnRMuufe7aQDHYc'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)

jwt = JWTManager(app)

# jwt custom decorator
# @jwt.user_claims_loader # Terima kasih atas perjuangan anda
# def add_claims_to_access_token(identity):
#     return {
#         'claims': identity,
#         'identifier': 'ATA-Batch3'
#     }

# Buat Decorator untuk internal only


def internal_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if not claims['status']:  # If berjalan jika statement True, jadi 'not False' = True
            return {'status': 'FORBIDDEN', 'message': 'Internal Only'}, 403
        else:
            return fn(*args, **kwargs)
    return wrapper

# Buat Decorator untuk non-internal


def non_internal_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if claims['status']:  # If berjalan jika statement True, jadi 'not False' = True
            return {'status': 'FORBIDDEN', 'message': 'Non-Internal Only'}, 403
        else:
            return fn(*args, **kwargs)
    return wrapper


# Setting Database
app.config['APP_DEBUG'] = True
# localhost aka 127.0.0.1
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:Altabatch3@ecommerce.ctfwww9400s4.ap-southeast-1.rds.amazonaws.com:3306/ecommerce'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# log error (middlewares)
@app.after_request
def after_request(response):
    try:
        requestData = request.get_json()
    except Exception as e:
        requestData = request.args.to_dict()

    app.logger.warning("REQUEST_LOG\t%s",
                       json.dumps({
                           'method': request.method,
                           'code': response.status,
                           'uri': request.full_path,
                           'request': requestData,
                           'response': json.loads(response.data.decode('utf-8'))
                       }))
    return response


# import blueprints
# Tidak perlu nama file, karena nama filenya __init__.py
from blueprints.auth import bp_auth
from blueprints.admin.resources import bp_admin
from blueprints.cart.resources import bp_cart
from blueprints.client.resources import bp_client
from blueprints.client_detail.resources import bp_client_detail
from blueprints.product.resources import bp_product
from blueprints.transaction.resources import bp_transaction
from blueprints.transaction_detail.resources import bp_transaction_detail
from blueprints.wishlish.resources import bp_wishlist

app.register_blueprint(bp_auth, url_prefix='/token')
app.register_blueprint(bp_admin, url_prefix='/admin')
app.register_blueprint(bp_cart, url_prefix='/cart')
app.register_blueprint(bp_client, url_prefix='/client')
app.register_blueprint(bp_client_detail, url_prefix='/client/detail')
app.register_blueprint(bp_product, url_prefix='/product')
app.register_blueprint(bp_transaction, url_prefix='/transaction')
app.register_blueprint(bp_wishlist, url_prefix='/wishlist')
app.register_blueprint(bp_transaction_detail, url_prefix='/transactiondetail')

db.create_all()
