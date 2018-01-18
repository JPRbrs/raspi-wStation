from flask import render_template

from app import app
from dbi import get_latest
from models import Instant


@app.route('/')
def index():
    """Serve the index HTML"""
    # instant = get_latest()
    instant = Instant(temperature=1, humidity=2, timestamp='2017-1-1')
    return render_template('index.html', instant=instant)
