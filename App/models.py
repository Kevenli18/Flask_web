#!_*_coding: utf-8 _*_
# @author =  lijun
# date  =  2018/7/10/010 10:08
from App.ext import db


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_name = db.Column(db.String(16))







