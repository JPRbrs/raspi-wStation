from flask import Flask

from flask_sqlalchemy import SQLAlchemy

DB_PATH = "/home/javier/projects/raspi-wStation/home.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////{}'.format(DB_PATH)
db = SQLAlchemy(app)

from app import views
