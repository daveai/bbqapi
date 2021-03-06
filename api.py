from flask import Flask
from flask_migrate import Migrate
from flask_restful import Resource, Api
from resources.User import User, Users
from db import setup_database
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:harry@localhost/bbq'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api.add_resource(Users, '/users', endpoint='users_ep')
api.add_resource(User, '/user/<int:user_id>', endpoint='user_ep')
if __name__ == '__main__':
	setup_database(app)
	app.run(debug=True)