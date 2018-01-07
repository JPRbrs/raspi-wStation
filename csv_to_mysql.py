import csv
from server import DB_PATH

def build_date_stamp(row):
    pass


def build_time_stamp(row):
    pass


def get_temp_hum_from_row(row):
    pass


def save_register_to_db(date_for_db, time_for_db, temp, hum):
    pass


def process_csv_row(row):
    date_for_db = build_date_stamp(row)
    time_for_db = build_time_stamp(row)
    temp, hum = get_temp_hum_from_row(row)
    save_register_to_db(date_for_db, time_for_db, temp, hum)


with open('data.csv', 'r') as data:
    reader = csv.reader(data)
    for row in reader:
        process_csv_row(row)
