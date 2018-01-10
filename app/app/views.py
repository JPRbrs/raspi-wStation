from flask import render_template

from app import app


@app.route('/')
def index():
    """Serve the index HTML"""
    from dbi import get_instants
    instants = get_instants()
    return render_template('index.html', instants=instants)
