import datetime
import pytest

from app.dbi import get_last_week
from app.models import Day

from dateutil import parser


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
