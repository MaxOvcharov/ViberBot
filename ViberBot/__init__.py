# -*- coding: utf-8 -*-

from flask import Flask
from database import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('ViberBot.config.config')
    db.init_app(app)
    with app.app_context():
        # Extensions like Flask-SQLAlchemy now know what the "current" app
        # is while within this block. Therefore, you can now run........
        db.create_all()
    return app
