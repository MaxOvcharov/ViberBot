from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from database import db
from simpleViberBot.simpleViberBot import app


app.config.from_object('ViberBot.config.config')
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
