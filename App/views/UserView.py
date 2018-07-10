#!_*_coding: utf-8 _*_
# @author =  lijun
# date  =  2018/7/10/010 14:48
from time import sleep

from flask import Blueprint, request, render_template, session

from App.ext import cache

blue = Blueprint('blue', __name__)



@blue.route('/index/')
@cache.cached(timeout=60)
def index():
    sleep(5)
    return 'this is a cache_test!'


@blue.route('/users/', methods=['GET', 'POST', 'DELETE', 'PUT'])
def users():
    if request.method == 'GET':
        return render_template('UserRegister.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        session['username'] = username
        return '注册成功！'
    elif request.method == 'PUT':
        username = session.get('username', 'not exist')
    return username


@blue.route('/set/')
def set():
    session['key'] = 'value'
    return 'ok'


@blue.route('/get/')
def get():
    return session.get('key', 'not set')


@blue.before_request   #请求前，类似django的中间件
def before():
    print('请求前')


@blue.route("/request/")
def reque():
    print('正在执行视图函数')
    return 'HELLO, AOP'


# @blue.after_request
# def after():
#     print("请求完成了")


