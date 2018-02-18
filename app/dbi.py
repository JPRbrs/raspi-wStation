from models import (
    Day,
    Instant,
)

from app import db
from datetime import (
    date,
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
        Instant.timestamp > '2018-01-01').all()
    return last_week


def get_day(year, month, day):
    date_obj = date(year, month, day)

    date_filter = '{}-{}-{}%'.format(
        year,
        str(month).zfill(2),
        str(day).zfill(2)
    )
    instants = Instant.query.filter(Instant.timestamp.like(date_filter)).all()

    day = Day(date_obj, instants)
    return day


def get_all_instants():
    return Instant.query.all()
