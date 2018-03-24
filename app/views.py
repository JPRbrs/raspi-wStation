xfrom flask import (
    jsonify,
    request,
    render_template,
)

from app import app

from app.dbi import (
    get_day,
    get_latest,
    get_month
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

    instant = get_latest()
    return render_template('indoor.html', instant=instant)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_day_ajax', methods=['POST'])
def get_dat_ajax():
    date = request.json['date']

    return jsonify(get_day(date).toJSON())


@app.route('/get_month_ajax', methods=['POST'])
def get_month_ajax():
    date = request.json['date']

    return jsonify(get_month(date).toJSON())
