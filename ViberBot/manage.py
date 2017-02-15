from flask_script import Manager
from . import create_app
from flask_migrate import MigrateCommand


manager = Manager(create_app)
manager.add_option("-c", "--config", dest="config_module", required=False)
manager.add_command('db', MigrateCommand)
