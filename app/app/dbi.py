from models.models import Instant
# from app.dth import get_hum_and_temp
from app import db
from datetime import datetime


def save_instant():
    # t, h = get_hum_and_temp()
    t, h = 1, 2
    timestamp = datetime.now().isoformat()
    i = Instant(temperature=t, humidity=h, timestamp=timestamp)
    db.session.add(i)
    db.session.commit()


def test():
    i = Instant(temperature=1, humidity=2, timestamp='2017-1-1')
    db.session.add(i)
    db.session.commit()


def get_all_instants():
    return Instant.query.all()