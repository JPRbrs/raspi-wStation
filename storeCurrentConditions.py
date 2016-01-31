from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ambient_declarative import Instant, Base
from DHT import requestData

database = 'home/git/lcd/ambient_readings.db'

engine = create_engine('sqlite:///' + database)

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

#Insert an instant in the table
data = requestData()
new_instant = Instant(**data)
session.add(new_instant)
session.commit()

