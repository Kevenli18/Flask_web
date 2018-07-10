#!_*_coding: utf-8 _*_
# @author =  lijun
# date  =  2018/7/10/010 19:45
from flask_restful import Resource


class HelloResource(Resource):
    def get(self):
        return {'hello': 'get'}

    def post(self):
        return {'hello': 'post'}

    def put(self):
        return {'hello': 'put'}

