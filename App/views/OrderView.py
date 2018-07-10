#!_*_coding: utf-8 _*_
# @author =  lijun
# date  =  2018/7/10/010 19:21

from flask import Blueprint

order = Blueprint('order', __name__)

@order.route('/order/')
def get_order():
    return 'this is a order'









