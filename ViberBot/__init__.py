# -*- coding: utf-8 -*-

from flask import Flask

from ViberBot.ViberBot.config import config
from database import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    return app
