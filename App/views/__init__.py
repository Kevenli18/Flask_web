#!_*_coding: utf-8 _*_
# @author =  lijun
# date  =  2018/7/10/010 10:08

from flask import Blueprint
from App.models import UserModel  #生成表,就可以迁移


#懒加载，后初始化的方式
from App.views.OrderView import order
from App.views.UserView import blue


def init_blueprint(app):
    app.register_blueprint(blueprint=blue)
    app.register_blueprint(blueprint=order)







