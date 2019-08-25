from blueprints import db
from flask_restful import fields

# CLIENT CLASS


class Clients(db.Model):
    __tablename__ = "client"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    status = db.Column(db.Boolean, nullable=False)


    response_fields_client_detail = {
        'id': fields.Integer,
        'username': fields.String,
        'password': fields.String,
        'email': fields.String,
        'status': fields.Boolean
    }

    response_fields_jwt = {
        'id': fields.String,
        'username': fields.String,
        'email': fields.String,
        'status': fields.Boolean
    }

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.status = False

    def __repr__(self):
        return '<Client %r>' % self.id
