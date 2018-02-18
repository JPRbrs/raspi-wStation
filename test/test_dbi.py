import datetime

from app.dbi import get_day


class TestGetDay():

    def test_get_day(self):
        day = get_day(2018, 1, 1)

        assert day is not None
        assert day.date == datetime.date(2018, 1, 1)
        # 12 hours * (60 minutes / 5 minutes each instant) = 288
        assert len(day.instants) == 288
