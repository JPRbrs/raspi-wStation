from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/javier/projects/'\
                                        'raspi-wStation/test.db'
db = SQLAlchemy(app)
