from flask_migrate import MigrateCommand
from flask_script import Manager

from App import create_app

app = create_app()

manager = Manager(app)
manager.add_command('db', MigrateCommand)   #注册可以使用命令行

if __name__ == '__main__':
    manager.run()






