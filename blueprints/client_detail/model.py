from blueprints import db
from flask_restful import fields

# CLIENT CLASS


class ClientDetails(db.Model):
    __tablename__ = "client_details"
    client_id = db.Column(db.Integer, primary_key = True, nullable = False)
    fullname = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(200), nullable=False)

    response_fields = {
        'client_id': fields.Integer,
        'fullname': fields.String,
        'phone': fields.String,
        'address': fields.String,
    }


    def __init__(self, client_id, fullname, phone, address):
        self.client_id = client_id
        self.fullname = fullname
        self.phone = phone
        self.address = address

    # def __repr__(self):
    #     return '<ClientDetails %r>' % self.client_id
