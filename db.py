from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
db = SQLAlchemy()


def setup_database(app):
    with app.app_context():
        db.init_app(app)
        db.create_all()
    # migrate = Migrate(app, db)
