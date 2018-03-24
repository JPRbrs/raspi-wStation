from models import (
    Day,
    Instant,
    OutdoorInstant,
)

from app import db
from datetime import (
    datetime,
    timedelta,
)

from weather import get_weather

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


def save_outdoor_instant():
    current_out_conditions = get_weather()
    out_instant = OutdoorInstant(
        temperature=current_out_conditions['out_temperature'],
        humidity=current_out_conditions['out_humidity'],
        feels_like=current_out_conditions['feels_like'],
        wind_speed=current_out_conditions['wind_speed'],
        timestamp=datetime.now().isoformat()
    )

    db.session.add(out_instant)
    db.session.commit()


def get_latest():
    return Instant.query.order_by(Instant.timestamp.desc()).first()


def get_last_week():
    last_week = db.session.query(Instant).filter(
        Instant.timestamp > '2018-01-01').all()
    return last_week


def get_day(date):
    instants = Instant.query.filter(
        Instant.timestamp.like('{}%'.format(date))).all()

    outdoor_instants = OutdoorInstant.query.filter(
        OutdoorInstant.timestamp.like('{}%'.format(date))).all()

    day = Day(date, instants, outdoor_instants)

    return day


def get_all_instants():
    return Instant.query.all()
