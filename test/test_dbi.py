import datetime

from app.dbi import (
    get_day,
    get_number_of_days_in_month,
    zfill_int,
)


class TestGetDay():

    def test_get_day(self):
        day = get_day('2018-03-15')

        assert day is not None
        assert day.date == datetime.date(2018, 3, 15)
        # 12 hours * (60 minutes / 5 minutes each instant) = 288
        assert len(day.instants) == 288


class TestUtils():

    def test_get_number_of_days_in_month(self):
        date = '2018-01-15'

        assert get_number_of_days_in_month(date) == 31

    def test_zfill_int(self):
        assert zfill_int(2) == '02'
        assert zfill_int(21) == '21'
