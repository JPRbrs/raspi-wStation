from .. import db


class Instant(db.Model):
    __tablename__ = 'instants'
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return '<Instant: {}>'.format(self.timestamp)
