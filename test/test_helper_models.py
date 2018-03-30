import datetime
import pytest
from random import randint

from app.helper_models import (
    Day,
    AbsInstant
)

from dateutil import parser


def generate_timestamps():
    base_timestamp = '2018-03-30T{}:{}:24.279411'
    for hour in range(0, 24):
        for minute in range(0, 60, 5):
            hour_str = str(hour).zfill(2)
            min_str = str(minute).zfill(2)
            yield base_timestamp.format(hour_str, min_str)


def generate_instant(timestamp):
    return AbsInstant(
        timestamp=timestamp,
        temperature=randint(10, 15),
        humidity=randint(40, 60)
    )


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


class TestDay:

    date = datetime.date(2018, 1, 22)

    def build_day(self):
        instants = get_last_week()
        instants = [
            i for i in get_last_week()
            if parser.parse(i.timestamp).date() == self.date
        ]
        return Day(self.date, instants)

    def test_constructor(self):
        day = self.build_day()

        for instant in day.instants:
            assert parser.parse(instant.timestamp).date() == self.date

    @pytest.mark.parametrize("attr, expected", [
        ('temperature', 20.1),
        ('humidity', 44.7)
    ])
    def test_temp_average(self, attr, expected):
        day = self.build_day()
        assert day.day_average(attr) == expected
