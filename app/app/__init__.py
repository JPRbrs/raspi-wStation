from flask import (
    Flask,
    render_template,
)
from flask_sqlalchemy import SQLAlchemy

DB_PATH = "/home/javier/projects/raspi-wStation/home.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////{}'.format(DB_PATH)
db = SQLAlchemy(app)


@app.route('/')
def index():
    """Serve the index HTML"""
    from dbi import get_instants
    instants = get_instants()
    return render_template('index.html', instants=instants)
