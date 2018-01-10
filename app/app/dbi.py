from models.models import Instant
from app import db


def test():
    i = Instant(temperature=1, humidity=2, timestamp='2017-1-1')
    db.session.add(i)
    db.session.commit()


def get_instants():
    return Instant.query.all()
