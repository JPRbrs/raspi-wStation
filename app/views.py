from flask import (
    jsonify,
    request,
    render_template,
)

from app import app
from models import Instant
from app.dbi import (
    get_day,
)
from weather import (
    get_forecast,
    get_weather,
)
from secrets import portcullis
from buses import get_next_bus


@app.route('/buses')
def buses():
    """
    Show next buses
    """
    next_bus = get_next_bus(stop_id=portcullis['primaryCode'], max_items=1)
    bus = {
        'number': next_bus['groupID'],
        'time': next_bus['timeLabel']
    }
    return render_template('buses.html', bus=bus)


@app.route('/outdoor')
def outdoor():
    """
    Shows outdoor conditions
    """
    return render_template('outdoor.html',
                           today=get_weather(),
                           forecast=get_forecast(1))


@app.route('/home_weather')
def home_weather():
    """Page showing indoor temp and hum"""

    # instant = get_latest()
    instant = Instant(temperature=1, humidity=2, timestamp='2017-1-1')
    return render_template('indoor.html', instant=instant)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ajax_call', methods=['POST'])
def ajax():
    date = request.json['date']

    return jsonify(get_day(date).toJSON())
