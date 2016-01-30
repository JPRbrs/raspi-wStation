from ambient_declarative import Instant, Base
from sqlalchemy import create_engine
from sqlalchemy import and_

database = 'ambient_readings.db'

engine = create_engine('sqlite:///' + database)

Base.metadata.bind = engine

from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

#Make a query to find all instants
#session.query(Instant).all()

#Make a query to find Instants lower than a given dates
retval = session.query(Instant).filter(Instant.id<3)
for x in range(retval.count()):
    print retval[x].id, retval[x].temp, retval[x].hum

#Make a query to find Instants betweenn two given dates
retval = session.query(Instant).filter(and_(Instant.id > 1, Instant.id < 3))
for x in range(retval.count()):
    print retval[x].id
