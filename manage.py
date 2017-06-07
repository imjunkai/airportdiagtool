from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from seeds import run, clear

from app import app, db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def seed():
    print('Seeding data...')
    run()

@manager.command
def unseed():
    print('Clearing seed data...')
    clear()

if __name__ == '__main__':
    manager.run()