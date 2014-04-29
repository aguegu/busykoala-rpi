# -*- coding: utf-8 -*-

import os
from app import app

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
basedir = app.root_path
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

THERMOMETER_PATH = '/sys/bus/w1/devices/28-00000535631e/w1_slave'
THERMOMETER_SCALE = 16
