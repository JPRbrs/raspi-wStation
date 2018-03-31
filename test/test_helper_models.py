import datetime
import pytest
from random import randint

from app.helper_models import (
    Day,
    AbsInstant
)

from dateutil import parser

BASE_TIMESTAMP = '2018-03-30T{}:{}:24.279411'


def generate_timestamps(timestamp=BASE_TIMESTAMP):
    for hour in range(0, 24):
        for minute in range(0, 60, 5):
            hour_str = str(hour).zfill(2)
            min_str = str(minute).zfill(2)
            yield timestamp.format(hour_str, min_str)


def generate_instant(timestamp):
    return AbsInstant(
        timestamp=timestamp,
        temperature=randint(10, 15),
        humidity=randint(40, 60)
    )


def generate_day():
    instants = []
    outdoor_instants = []

    for timestamp in generate_timestamps():
        instants.append(generate_instant(timestamp))
        outdoor_instants.append(generate_instant(timestamp))

    return Day(timestamp, instants, outdoor_instants)


class TestHelpers:

    def test_generate_instant(self):
        timestamp = generate_timestamps().next()
        instant = generate_instant(timestamp)

        assert instant.timestamp == timestamp
        assert instant.temperature is not None
        assert instant.humidity is not None

    def test_generate_timestamps(self):
        timestamps = [t for t in generate_timestamps()]

        assert timestamps[0] == '2018-03-30T00:00:24.279411'
        assert timestamps[len(timestamps) - 1] == '2018-03-30T23:55:24.279411'
        assert len(timestamps) == 288

    def test_generate_day(self):
        day = generate_day()

        assert len(day.instants) == 288
        assert len(day.outdoor_instants) == 288  # Check it has all params
        assert day.date is not None
