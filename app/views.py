from flask import render_template, make_response, send_file, jsonify, request

from app import app
from models import Instant
from app.dbi import (
    get_day,
    get_last_week,
)
from weather import get_weather


@app.route('/testing')
def index_testing():
    """
    Serve index when running outside of the pi
    """
    instant = Instant(temperature=1, humidity=2, timestamp='1979-01-01')
    return render_template('index_testing.html', instant=instant)


@app.route('/outdoors')
def outdoors():
    """
    Shows outdoors conditions
    """
    return render_template('outdoors.html', today=get_weather())


@app.route('/home_weather')
def home_weather():
    """Page showing indoor temp and hum"""

    # instant = get_latest()
    instant = Instant(temperature=1, humidity=2, timestamp='2017-1-1')
    return render_template('indoor.html', instant=instant)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/last_week')
def last_week():
    """
    Test endpoint
    """
    instants_last_week = get_last_week()
    return render_template('last_week.html',
                           instants_last_week=instants_last_week)


@app.route("/simple.png")
def simple():
    import datetime
    import StringIO
    import random

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    fig = Figure()
    ax = fig.add_subplot(111)
    x = []
    y = []
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now += delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas = FigureCanvas(fig)
    png_output = StringIO.StringIO()
    canvas.print_png(png_output)
    response = make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'

    fig.savefig(png_output)
    png_output.seek(0)
    return send_file(png_output, mimetype='image/png')


@app.route('/ajax_call', methods=['POST'])
def ajax():
    date = request.json['date']

    return jsonify(get_day(date).toJSON())


@app.route('/test_one_day')
def test_one_day():
    day = get_day((2017, 9, 20))

    return render_template('test_one_day.html', day=day)


@app.route('/d3')
def d3():
    day = get_day('2017-09-20')

    my_data = [{'time': i.timestamp,
                'name': 'temperature',
                'value': i.temperature}
               for i in day.instants]

    return render_template('d3.html', my_data=my_data)
