from datetime import datetime
from time import sleep

from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import weather

from app import app, db
from app.dht import get_hum_and_temp
from app.dbi import save_instant
from lcd import LCD

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
    temp, hum = get_hum_and_temp()
    time = datetime.now().strftime('%H:%M')
    weather_dict = weather.get_weather()
    line1 = "{0:0.1f} C and {1:0.1f}%".format(temp, hum)
    line2 = time + " Feels %d" % (
        int(weather_dict['out_feel'])
    )
    try:
        lcd = LCD()
        sleep(0.5)
        lcd.send_text(line1, 1)
        lcd.send_text(line2, 2)
    except Exception, e:
        print e
        lcd._clean_up()
        quit()
    except KeyboardInterrupt:
        print 'User interrupted'
        lcd._clean_up()
        quit()


#if __name__ == "__main__":
#    manager.run()
