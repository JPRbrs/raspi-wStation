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
