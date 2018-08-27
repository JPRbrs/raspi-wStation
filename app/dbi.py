import logging
import logging.config

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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(levelname)-8s:%(name)-20s: %(message)s '
            '(%(asctime)s; %(filename)s:%(lineno)d)',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}

logging.config.dictConfig(LOGGING)

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
    '''Gets all instants from the database for requested_date (with format
    yy-mm-dd), creates a DayCreator instance and pupulates a Day instance

    '''
    instants = Instant.query.filter(
        Instant.timestamp.like('{}%'.format(requested_date))
    ).all()

    outdoor_instants = OutdoorInstant.query.filter(
        OutdoorInstant.timestamp.like('{}%'.format(requested_date))).all()

    year, month, day = map(int, requested_date.split('-'))
    requested_date = date(year, month, day)
    day = DayCreator(requested_date, instants, outdoor_instants)

    return day


def store_day(date):
    day = get_day(date).toJSON()

    day_db_model = Day(
        date=day['date'],
        indoor_avg_temp=day['indoor_avg_temp'],
        indoor_avg_hum=day['indoor_avg_hum'],
        outdoor_avg_temp=day['outdoor_avg_temp'],
        outdoor_avg_hum=day['outdoor_avg_hum']
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
    logging.info("Entering get_month")
    days = Day.query.filter(Day.date.contains(requested_date[0:-3])).all()

    instants = []
    outdoor_instants = []

    for day in days:
        instants.append({
            'timestamp': day.date,
            'temperature': day.indoor_avg_temp,
            'humidity': day.indoor_avg_hum
        })

        outdoor_instants.append({
            'timestamp': day.date,
            'temperature': day.outdoor_avg_temp,
            'humidity': day.outdoor_avg_hum
        })

    logging.info("Days returned = {}".format(len(days)))

    return {
        'instants': instants,
        'outdoor_instants': outdoor_instants,
        'total_days': len(days)
    }


def get_all_instants():
    return Instant.query.all()


def timestamp_to_datetime(timestamp):
    try:
        ret_val = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f")
    except ValueError:
        ret_val = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S")

    return ret_val
