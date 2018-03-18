from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


DB_PATH = "/home/javier/projects/raspi-wStation/home.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////{}'.format(DB_PATH)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

import views  # NOQA
import models # NOQA
