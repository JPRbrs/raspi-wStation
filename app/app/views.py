from flask import render_template

from app import app


@app.route('/')
def index():
    """Serve the index HTML"""
    from dbi import get_all_instants
    instants = get_all_instants()
    return render_template('index.html', instants=instants)
