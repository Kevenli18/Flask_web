#!_*_coding: utf-8 _*_
# @author =  lijun
# date  =  2018/7/10/010 19:46
from flask_restful import Resource


class UserResource(Resource):
    def get(self):
        return {'msg': 'user get'}

    def post(self):
        return {'msg': 'user post'}





