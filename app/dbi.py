from models import (
    AbsInstant,
    Instant,
    OutdoorInstant,
)


from app import db
from app.helper_models import DayCreator
from app.models import Day
from datetime import (
    datetime,
    date,
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


def get_day(requested_date):
    # Receives data in format yy-mm-dd
    instants = Instant.query.filter(
        Instant.timestamp.like('{}%'.format(requested_date))).all()

    outdoor_instants = OutdoorInstant.query.filter(
        OutdoorInstant.timestamp.like('{}%'.format(requested_date))).all()

    year, month, day = map(int, requested_date.split('-'))
    requested_date = date(year, month, day)
    day = DayCreator(requested_date, instants, outdoor_instants)

    return day


def store_day(date):
    day = get_day(date).to_json()

    day_db_model = Day(
        day['date'],
        day['indoor_avg_temp'],
        day['indoor_avg_hum'],
        day['outdoor_avg_temp'],
        day['outdoor_hum_avg']
    )

    db.session.add(day_db_model)
    db.session.commit()


def get_number_of_days_in_month(date_string):
    # date received in format yy-mm-dd
    year, month, day = map(int, date_string.split('-'))
    month_start = date(year, month, 1)
    next_month_start = date(year, month + 1, 1)

    return (next_month_start - month_start).days


def zfill_int(number):
    return str(number).zfill(2)


def get_month(requested_date):
    """
    This functions receives a string in format yy-mm-dd
    """

    year, month, day = map(int, requested_date.split('-'))
    # Get all instants for given month
    search_date = requested_date[:4]
    instants = Instant.query.filter(
        Instant.timestamp.like('{}%'.format(search_date))).all()
    outdoor_instants = OutdoorInstant.query.filter(
        OutdoorInstant.timestamp.like('{}%'.format(search_date))).all()

    # Group instants by day
    days = []
    days_in_month = get_number_of_days_in_month(requested_date)
    for day in xrange(1, days_in_month + 1):
        day_date = date(year, month, day)
        in_instants = [i for i in instants if
                       timestamp_to_datetime(i.timestamp).date() == day_date]

        out_instants = [i for i in outdoor_instants if
                        timestamp_to_datetime(i.timestamp).date() == day_date]

        days.append(DayCreator(day_date.strftime('%d-%m-%Y'), in_instants,
                        out_instants))

    # Calculate day averages so a month is "a day" where each instant is
    # a day_average
    avg_instants = []
    avg_outdoor_instants = []

    for day in days:
        averages = day.get_averages()
        avg_instants.append(AbsInstant(
            averages['date'],
            averages['indoor_temp_avg'],
            averages['indoor_hum_avg']))
        avg_outdoor_instants.append(AbsInstant(
            averages['date'],
            averages['outdoor_temp_avg'],
            averages['outdoor_hum_avg']))

    return DayCreator(requested_date, avg_instants, avg_outdoor_instants)


def get_all_instants():
    return Instant.query.all()


def timestamp_to_datetime(timestamp):
    try:
        ret_val = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f")
    except ValueError:
        ret_val = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S")

    return ret_val
