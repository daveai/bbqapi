from flask import jsonify
from flask_restful import Resource
from models.User import UserModel
from models.User import UserSchema
from flask import request


class Users(Resource):

    def get(self):
        all_users = UserModel.query.all()
        user_schema = UserSchema(many=True)
        result = user_schema.dump(all_users)
        return jsonify(result.data)

    def post(self):
        email = request.authorization.username
        password = request.authorization.password
        user = UserModel.query.filter(UserModel.user_email == email).filter(UserModel.user_pass == password).first()
        if user:
            user_schema = UserSchema()
            result = user_schema.dump(user)
            return jsonify(result.data)
        return {}, 404


class User(Resource):
    def get(self,user_id):
        user = UserModel.query.filter(UserModel.ID==user_id).first()
        user_schema = UserSchema()
        result = user_schema.dump(user)
        return jsonify(result.data)