import datetime

from app.dbi import (
    get_day,
    get_number_of_days_in_month,
    zfill_int,
)


class TestGetDay():

    def test_get_day(self):
        day = get_day(2018, 1, 1)

        assert day is not None
        assert day.date == datetime.date(2018, 1, 1)
        # 12 hours * (60 minutes / 5 minutes each instant) = 288
        assert len(day.instants) == 288


class TestUtils():

    def test_get_number_of_days_in_month(self):
        date_object = datetime.date(2018, 1, 1)

        assert get_number_of_days_in_month(date_object) == 31

    def test_zfill_int(self):
        assert zfill_int(2) == '02'
        assert zfill_int(21) == '21'
