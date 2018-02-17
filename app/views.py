from flask import render_template, make_response, send_file, jsonify

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

    # return response


@app.route('/ajax_call', methods=['POST'])
def ajax():
    i = Instant(temperature=1,
                humidity=2,
                timestamp='aasdfasd')
    return jsonify(i.toJSON())
