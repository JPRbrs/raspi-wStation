from models import Instant
from dht import get_hum_and_temp
from app import db
from datetime import (
    datetime,
    timedelta,
)


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


def get_all_instants():
    return Instant.query.all()
