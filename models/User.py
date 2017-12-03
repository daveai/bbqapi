from db import db
from sqlalchemy import exc
from db import ma


class UserModel(db.Model):
    __tablename__ = 'b_users'
    ID = db.Column(db.Integer, primary_key=True)
    user_login = db.Column(db.String(120), nullable=False)
    user_pass = db.Column(db.String(120), nullable=False)
    user_nicename = db.Column(db.String(120), nullable=False)
    user_email = db.Column(db.String(120), nullable=False)
    user_url = db.Column(db.String(120), nullable=False)
    user_registered = db.Column(db.String(120), nullable=False)
    user_activation_key = db.Column(db.String(120), nullable=False)
    user_status = db.Column(db.Integer, nullable=False)
    display_name = db.Column(db.String(120), nullable=False)
class UserSchema(ma.Schema):
    class Meta:
        fields = ('ID', 'user_login', 'user_nicename', 'user_email', '_links')

    _links = ma.Hyperlinks({
        'self': ma.URLFor('user_ep', user_id='<ID>')
    })