#!_*_coding: utf-8 _*_
# @author =  lijun
# date  =  2018/7/10/010 16:44
from flask_restful import Api

from App.apis.HelloApi import HelloResource
from App.apis.UserApi import UserResource

api = Api()


def init_api(app):
    api.init_app(app=app)


api.add_resource(HelloResource, '/hello/')
api.add_resource(UserResource, '/user/')




