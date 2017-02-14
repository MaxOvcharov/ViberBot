# -*- coding: utf-8 -*-

from flask import Flask

from ViberBot.db_conf import db
from simpleViberBot import simpleViberBot
app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

