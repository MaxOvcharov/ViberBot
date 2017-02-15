# -*- coding: utf-8 -*-

from flask import Flask
from database import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('ViberBot.config.config')
    db.init_app(app)
    return app
