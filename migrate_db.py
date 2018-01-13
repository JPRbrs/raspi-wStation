import csv
from datetime import datetime
from app.app import db
from app.app.models.models import Instant


def build_timestamp(row):
    datetime_instant = datetime(int(row[5]), int(row[4]),
                                int(row[3]), int(row[6]),
                                int(row[7]))
    return datetime_instant.isoformat()


def process_csv_row(row):
    timestamp = build_timestamp(row)
    temp = row[1]
    hum = row[2]
    instant = Instant(temperature=temp,
                      humidity=hum,
                      timestamp=timestamp)

    db.session.add(instant)
    db.session.commit()


def process_csv_file():
    with open('data.csv', 'r') as data:
        reader = csv.reader(data)
        for row in reader:
            process_csv_row(row)


if __name__ == '__main__':
    process_csv_file()
