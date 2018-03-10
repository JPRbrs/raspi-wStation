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

    json_attributes = (
        'temperature',
        'humidity',
        'timestamp'
    )

    def __repr__(self):
        return '<OutdoorInstant: {}>'.format(self.timestamp)

    def toJSON(self):
        return {
            key: getattr(self, key) for key in self.json_attributes
        }


class Day(object):

    def __init__(self, date, instants):
        self.date = date
        self.instants = instants

    def __repr__(self):
        return '<Day: {}>'.format(self.date)

    def day_average(self, attr):
        total = 0
        for instant in self.instants:
            total += getattr(instant, attr)
        average = total / len(self.instants)
        return round(average, 1)

    def toJSON(self):
        return {
            'date': self.date,
            'instants': [i.toJSON() for i in self.instants]
        }
