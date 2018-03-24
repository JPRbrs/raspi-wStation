from models import (
    Day,
    Instant,
    OutdoorInstant,
)

from app import db
from datetime import (
    datetime,
    timedelta,
    date,
)

from dateutil.parser import parse

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


def get_number_of_days_in_month(date_object):
    month_start = date(date_object.year, date_object.month, 1)
    next_month_start = date(date_object.year, date_object.month + 1, 1)

    return (next_month_start - month_start).days


def zfill_int(number):
    return str(number).zfill(2)


def get_month(requested_date):
    """
    This functions receives a string in format yyyy-mm-dd
    """
    date = parse(requested_date).date()

    # Get all instants for given month
    search_date = date.strftime('%Y-%m')
    instants = Instant.query.filter(
        Instant.timestamp.like('{}%'.format(search_date))).all()
    outdoor_instants = OutdoorInstant.query.filter(
        OutdoorInstant.timestamp.like('{}%'.format(search_date))).all()

    # Group instants by day
    days = []
    days_in_month = get_number_of_days_in_month(date)
    for day in xrange(1, days_in_month + 1):
        day_date = '{}-{}-{}'.format(date.year, zfill_int(date.month), day)
        day_instants = [i for i in instants if i.timestamp[:9] == date]
        day_outdoor_instants = [i for i in outdoor_instants if
                                i.timestamp[:9] == date]
        days.append(Day(day_date, day_instants, day_outdoor_instants))

    import pdb; pdb.set_trace()

    return days


def get_all_instants():
    return Instant.query.all()
