from app import db


class AbsInstant(object):

    def __init__(self, timestamp, temperature, humidity):
        self.timestamp = timestamp
        self.temperature = temperature
        self.humidity = humidity

    json_attributes = (
        'temperature',
        'humidity',
        'timestamp'
    )

    def __repr__(self):
        return '<Instant: {}>'.format(self.timestamp)

    def toJSON(self):
        return {
            key: getattr(self, key) for key in self.json_attributes
        }


class Instant(db.Model):

    __tablename__ = 'instants'
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.String(25), nullable=False)

    json_attributes = (
        'temperature',
        'humidity',
        'timestamp'
    )

    def __repr__(self):
        return '<Instant: {}>'.format(self.timestamp)

    def toJSON(self):
        return {
            key: getattr(self, key) for key in self.json_attributes
        }


class OutdoorInstant(db.Model):
    # TODO: heredar de Instant

    __tablename__ = 'outdoor_instants'
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.String(25), nullable=False)
    feels_like = db.Column(db.Integer, nullable=False)
    wind_speed = db.Column(db.Integer, nullable=False)

    json_attributes = (
        'temperature',
        'humidity',
        'timestamp',
        'feels_like',
        'wind_speed'
    )

    def __repr__(self):
        return '<OutdoorInstant: {}>'.format(self.timestamp)

    def toJSON(self):
        return {
            key: getattr(self, key) for key in self.json_attributes
        }


class Day(object):

    def __init__(self, date, instants, outdoor_instants):
        self.date = date
        self.instants = instants
        self.outdoor_instants = outdoor_instants

    def __repr__(self):
        return '<Day: {}>'.format(self.date)

    def day_average(self, array, attr):
        total = 0

        for instant in array:
            total += getattr(instant, attr)
        if total != 0:
            average = total / len(array)
        else:
            average = 0

        return round(average, 1)

    def toJSON(self):
        return {
            'date': self.date,
            'instants': [i.toJSON() for i in self.instants],
            'outdoor_instants': [j.toJSON() for j in self.outdoor_instants],
            'indoor_temp_avg': self.day_average(self.instants, 'temperature'),
            'indoor_hum_avg': self.day_average(self.instants, 'humidity'),
            'outdoor_temp_avg': self.day_average(self.outdoor_instants,
                                                 'temperature'),
            'outdoor_hum_avg': self.day_average(self.outdoor_instants,
                                                'humidity')
        }

    def get_averages(self):
        return {
            'date': self.date,
            'indoor_temp_avg': self.day_average(self.instants, 'temperature'),
            'indoor_hum_avg': self.day_average(self.instants, 'humidity'),
            'outdoor_temp_avg': self.day_average(self.outdoor_instants,
                                                 'temperature'),
            'outdoor_hum_avg': self.day_average(self.outdoor_instants,
                                                'humidity')
        }
