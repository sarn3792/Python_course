from flask_restful import Resource, Api

class HelloWorld(Resource):
	def get(self):
		return {'hello' : 'world'}


class Users(Resource):
	def get(self):
		return {'hello' : 'users'}
