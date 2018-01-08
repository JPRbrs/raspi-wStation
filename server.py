from flask import (
    Flask,
    render_template,
)
from flask_sqlalchemy import SQLAlchemy

DB_PATH = "/home/javier/projects/raspi-wStation/home.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////{}'.format(DB_PATH)
db = SQLAlchemy(app)


class Instant(db.Model):
    __tablename__ = 'instants'
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return '<Instant: {}>'.format(self.timestamp)


def test():
    i = Instant(temperature=1, humidity=2, timestamp='2017-1-1')
    db.session.add(i)
    db.session.commit()


@app.route('/')
def index():
    """Serve the index HTML"""
    return render_template('index.html')
