from flask_restful import Resource
from flask import request

class Get_holdings(Resource):
    def post(self):
        rec_data = request.json