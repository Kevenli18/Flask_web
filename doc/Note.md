-请求流程
    -browser->router(在应用上，使用装饰器实现)-

#### Flask-Script
-让Flask项目支持命令行参数
-使用流程
    安装
        -pip install flask-script
    初始化
        manage = Manager（app）
    使用
        -调用参数
        -h  指定主机
        -p  指定端口
        -d  调试模式
        -r  自动重新加载

#### 项目拆分
-models
-views
-templates

#### Flask-Blueprint
-蓝图
    -美好的规划
-规划了请求
-使用流程
    -安装
        -pip install flask-blueprint
    -初始化
        -在app注册蓝图
    -使用蓝图注册路由
        -@blue.route('xx')

#### Flask-SQLAlchemy
-ORM框架
    -定义models
    -封装数据库的操作

#### Flask-Migrate
-迁移库
-实现数据库迁移
-使用流程
    -安装
        -pip install flask-migrate
    -初始化
        -创建一个migrate对象
        需要和models关联，SQLAlchemy对象关联
        需要和app关联
        和Flask-Script结合使用
            -在manager对象上添加指令
            -manager.add_commad('db', MigrateCommand)
    -使用
        -python manager.py db xxx
            -init 首次使用必须调用init
            -migrate 生成迁移文件
            -upgrade 迁移
            -downgrade



#### ext.py
-extension 扩展


#### 项目结构
-App
    -__init__项目主入口
    -setting.py 数据库连接
    -ext.py
        -统一管理第三方包
        -ORM,SQLAlchemy对象
        -衍生models
    -views
        -
-doc
-migrations
-manage.py
-requirement.txt
-venv
    -虚拟环境放在工程根目录
    -全局虚拟环境

#### Flask 四大内置对象
-request
-session
    -默认存在内存中
    -数据库中
    -缓存中（Redis）
    -文件中
    -cookie
-g
    -全局对象
    -传递数据
    -跨函数传递数据

-config
    -app.config
    -模板中直接使用config
    -在app需要获取到app对象，再获取config
        -

#### flask-session
-提供Flask中的session处理策略
-使用流程
    -pip install flask-session
    -初始化
    -指定SESSION-TYPE
    -使用
    -和原生session一样

#### Flask-Caching
-Flask-Cache中一样，但flask-cache不能用了，长期没更新
-使用流程
    -安装
        -pip install flask-caching
    -初始化
        -使用App构建cache对象
        -指定config
            -CACHE-TYPE, redis
        -使用
            -cache.cached()

#### Flask-RESTful
-
-安装
    -pip install flask-restful

-

#### 项目体系
-如果项目需要添加额外扩展库
    -直接在ext中添加
    -和路由相关的，独立出来
        -蓝图
        -restful api
-实现功能
    -建模（定义数据）
    -路由和视图函数
        -蓝图写法
            -每个功能都创建自己的一个蓝图
            -在app上注册蓝图
            -使用蓝图注册自己的功能
        -使用rest api
            -创建自己的resource
            -在api上注 册resource
    -返回
        -最终都是Resource
        -RESTAPI中




