#!_*_coding: utf-8 _*_
# @author =  lijun
# date  =  2018/7/10/010 10:07
from flask import Flask

from App.apis import init_api
from App.ext import init_ext
from App.setting import envs
from App.views import init_blueprint


def create_app():
    app = Flask(__name__)
    #初始化Flask config  配置文件
    app.config.from_object(envs.get('develop'))
    # 初始化 扩展库 migrate，SQLALCHEMY 注册插件ext是extends
    init_ext(app)
    #进入蓝图
    init_blueprint(app)

    #注册rest api
    init_api(app)
    return app






