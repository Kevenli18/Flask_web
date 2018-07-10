#!_*_coding: utf-8 _*_
# @author =  lijun
# date  =  2018/7/10/010 11:11

def get_db_url(dbinfo):
    #提供默认值
    DB = dbinfo.get('DB') or 'mysql'
    DRIVER = dbinfo.get('DRIVER') or 'pymysql'
    USER = dbinfo.get('USER') or 'root'
    PASSWORD = dbinfo.get('PASSWORD') or 'root'
    HOST = dbinfo.get('HOST') or 'localhost'
    PORT = dbinfo.get('PORT') or '3306'
    NAME = dbinfo.get('NAME') or 'mysql'
    return '{}+{}://{}:{}@{}:{}/{}'.format(DB, DRIVER, USER, PASSWORD, HOST, PORT, NAME)


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    DEBUG = True
    DATABASE = {
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'web_flask',
        'DB': 'mysql',
        'DRIVER': 'pymysql',
    }
    SQLALCHEMY_DATABASE_URI = get_db_url(DATABASE)
    SESSION_TYPE = 'redis'


class TestingConfig(Config):
    TESTING = True
    DATABASE = {
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'web_flask',
        'DB': 'mysql',
        'DRIVER': 'pymysql',
    }
    SQLALCHEMY_DATABASE_URI = get_db_url(DATABASE)


class StagingConfig(Config):
    DEBUG = True
    DATABASE = {
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'web_flask',
        'DB': 'mysql',
        'DRIVER': 'pymysql',
    }
    SQLALCHEMY_DATABASE_URI = get_db_url(DATABASE)


class ProductConfig(Config):
    DEBUG = True
    DATABASE = {
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'web_flask',
        'DB': 'mysql',
        'DRIVER': 'pymysql',
    }
    SQLALCHEMY_DATABASE_URI = get_db_url(DATABASE)


envs = {
    'develop': DevelopConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'product': ProductConfig,
    'default': DevelopConfig,
}


