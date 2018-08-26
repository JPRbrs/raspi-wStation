from datetime import datetime, date, timedelta
from time import sleep


from flask_script import (
    Manager,
)

try:
    from app.dht import get_hum_and_temp
except ImportError:
    print('Not running on the pi, some features won\'t be available')

from app.dbi import (
    save_instant,
    save_outdoor_instant,
    store_day
)
from lcd import LCD
import weather
from app import app
from flask_migrate import MigrateCommand

app.debug = True

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def store_indoor_instant():
    save_instant()


@manager.command
def store_yesterday_averages():
    yesterday = (date.today() - timedelta(hours=24)).strftime('%Y-%m-%d')
    store_day(yesterday)


@manager.command
def create_all_past_days():
    today = date.today()
    from datetime import date as date_
    first_day = date_(2017, 9, 7)

    day = first_day
    while day < today:
        store_day(day.strftime('%Y-%m-%d'))
        day += timedelta(days=1)


@manager.command
def store_outdoor_instant():
    save_outdoor_instant()


@manager.command
def cron_lcd():
    hum, temp = get_hum_and_temp()
    time = datetime.now().strftime('%H:%M')
    weather_dict = weather.get_weather()
    line1 = "{0:0.1f} C and {1:0.1f}%".format(temp, hum)
    line2 = time + " Feels %d" % (
        int(weather_dict['feels_like'])
    )
    try:
        lcd = LCD()
        sleep(0.5)
        lcd.send_text(line1, 1)
        lcd.send_text(line2, 2)
    except Exception:
        lcd._clean_up()
        raise


if __name__ == "__main__":
    manager.run()
