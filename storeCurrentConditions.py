from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import smtplib
import mimetypes
from email.message import Message
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

from ambient_declarative import Instant, Base
from DHT import requestData
import data

MAX_TEMP = 24
MAX_HUM = 60

def sendMail(subject, body):
    outer = MIMEMultipart()
    outer['Subject'] = subject
    outer['To'] = data.dict['hotmail']
    outer['From'] = data.dict['gmail']
    outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'

    #Proccess before attaching
    message_body = MImetext(body, 'plain')
    outer.attach(message_body)

    # Now send or store the message
    composed = outer.as_string()

    #server =  smtplib.SMTP('smtp.live.com:587')
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(data.dict['gmail'],data.dict['password'])
    problems=server.sendmail(outer['From'] , outer['To'], composed)
    server.quit()

def alert_conditions(data):
    if data['hum'] > MAX_HUM or data['temp'] > MAX_TEMP:
        body = 'Temperature or humidiy above maximum levels'
        subject = 'Ambient conditions alert'

        sendMail(subject, body)

engine = create_engine('sqlite:///' + data.dict['database'])

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

alert_conditions(data)

new_instant = Instant(**data)
session.add(new_instant)
session.commit()

