# -*- coding: utf-8 -*-

from flask import Flask

from simpleViberBot import simpleViberBot
from db_conf import db
app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

