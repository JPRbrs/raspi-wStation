from flask import render_template

from app import app
from models import Instant
from app.dbi import get_last_week


@app.route('/')
def index():
    """Serve the index HTML"""

    # instant = get_latest()
    instant = Instant(temperature=1, humidity=2, timestamp='2017-1-1')
    return render_template('index.html', instant=instant)


@app.route('/last_week')
def last_week():
    """
    Test endpoint
    """
    instants_last_week = get_last_week()
    return render_template('last_week.html',
                           instants_last_week=instants_last_week)
