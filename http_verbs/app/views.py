from app import app2
from flask_restful import Resource, Api
from app import controllers

api = Api(app2)

api.add_resource(controllers.HelloWorld, "/", "/index")
api.add_resource(controllers.Users, "/users")

