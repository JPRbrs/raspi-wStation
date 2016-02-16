import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from electric_declarative import PowerInstant, Base

def getDateForDatabase():
    parameters = ['year', 'month', 'day', 'hour', 'minute']
    dateCorrect = False

    while dateCorrect == False:
    #current date in seconds
        dateInSeconds = int(time.time())
        dateConstruct = time.gmtime(int(dateInSeconds))
        listDate = list(dateConstruct)

        for param in zip(range(5), parameters):
            default = str(listDate[param[0]])
            newValue = raw_input('Press enter to confirm: ' + default  + '(' + param[1] + '): ')
            if newValue != '':
                try:
                    listDate[param[0]] = int(newValue)
                except ValueError:
                    print "Wrong parameter, must be int"
                    quit()

        newDate=time.mktime(listDate)
        if raw_input("Confirm following date pressing enter: " +
                     time.strftime('%d-%b-%Y %H:%M',
                                   time.gmtime(int(newDate))) + " ") == '':
            dateCorrect = True

    return int(newDate)

database = '/home/pi/git/LCD/ambient_readings.db'

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
date = getDateForDatabase()
try:
    power = float(raw_input("Introduce power: "))
except ValueError:
    print "Invalid error. Must be float"
    quit()

print date, power
new_instant = PowerInstant(date=date, power=power)
session.add(new_instant)
session.commit()

