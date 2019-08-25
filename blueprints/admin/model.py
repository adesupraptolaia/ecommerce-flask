from blueprints import db
from flask_restful import fields

# ADMIN CLASS


class Admins(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    status = db.Column(db.Boolean, nullable=False)

    response_fields = {
        'id': fields.Integer,
        'username': fields.String,
        'email': fields.String,
        'status': fields.Boolean
    }

    def __init__(self, username, password, email):
        self.username =username
        self.password =password
        self.email =email
        self.status = True

    def __repr__(self):
        return '<Admin %r>' % self.id
