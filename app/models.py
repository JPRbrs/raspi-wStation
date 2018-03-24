from app import db


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

    def day_average(self, attr):
        total_indoor = 0
        total_outdoor = 0

        for instant in self.instants:
            total_indoor += getattr(instant, attr)
        average_indoor = total_indoor / len(self.instants)

        for instant in self.outdoor_instants:
            total_indoor += getattr(instant, attr)
        average_outdoor = total_outdoor / len(self.outdoor_instants)

        return (round(average_indoor, 1), round(average_outdoor, 1))

    def toJSON(self):
        return {
            'date': self.date,
            'instants': [i.toJSON() for i in self.instants],
            'outdoor_instants': [j.toJSON() for j in self.outdoor_instants]
        }
