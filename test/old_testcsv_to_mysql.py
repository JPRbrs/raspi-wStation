from csv_to_mysql import (
    build_timestamp,
)

ROW_SAMPLE = ['8479', '19.1', '58.4', '7', '10', '2017', '7', '0']


class TestCsvToMysql:
    def test_build_timestamp(self):
        result = build_timestamp(ROW_SAMPLE)
        assert result == '2017-10-07T07:00:00'
