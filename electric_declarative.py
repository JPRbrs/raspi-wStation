import os
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

database = '/home/pi/git/LCD/ambient_readings.db'


Base = declarative_base()

class PowerInstant(Base):
    __tablename__ = 'consumedPower'
    #Define columns
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Integer, nullable=False)
    power = Column(Integer, nullable=False)
    
# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///' + database)

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)

