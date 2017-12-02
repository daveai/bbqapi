from flask_restful import Resource, Api
from models.t1 import t1


class HelloWorld(Resource):
    def get(self):
        admin = t1(username='admin', email='admin@example.com', PIC='dfdfg')
        t1.insert(admin)
        return {'hello': 'world'}
