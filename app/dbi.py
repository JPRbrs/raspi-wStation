from models import Instant

from app import db
from datetime import (
    datetime,
    timedelta,
)

try:
    from dht import get_hum_and_temp
except ImportError:
    print('Not running on the pi, some features won\'t be available')


def save_instant():
    h, t = get_hum_and_temp()
    timestamp = datetime.now().isoformat()
    i = Instant(temperature=t, humidity=h, timestamp=timestamp)
    db.session.add(i)
    db.session.commit()


def get_latest():
    timestamp = datetime.now().isoformat()
    five_min_ago = (datetime.now() - timedelta(minutes=5)).isoformat()
    print(timestamp, five_min_ago)


def get_last_week():
    last_week = db.session.query(Instant).filter(
        Instant.timestamp > '2018-01-22').all()
    return last_week


def get_instants_from_month(year, month):
    month_filter = '{}-{}-%'.format(
        str(year).zfill(2),
        str(month).zfill(2))
    instants = Instant.query.filter(
        Instant.timestamp.like(month_filter)).all()
    return instants


def get_all_instants():
    return Instant.query.all()
