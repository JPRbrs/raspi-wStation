from datetime import datetime
from time import sleep

from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

try:
    from app.dht import get_hum_and_temp
except ImportError:
    print('Not running on the pi, some features won\'t be available')

from app import app, db
from app.dbi import save_instant
from lcd import LCD
import weather


migrate = Migrate(app, db)
app.debug = True

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///home.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def hello():
    print "hello"


@manager.command
def save_instant_into_db():
    save_instant()


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
