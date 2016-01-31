#!/usr/bin/python
import requests
from requests.auth import AuthBase
import hmac
import hashlib
import time
from celery import Celery

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

#define object
class InfoSpot(Base):
    __tablename__ = 'infospot'
    id= Column(Integer,primary_key=True)
    solid_rating = Column(Integer)
    faded_rating = Column(Integer)
    chart_wind_url = Column(String)
    chart_period_url = Column(String)
    wind_direction = Column(Integer)
    wind_compass_direction = Column(String)
    wind_speed = Column(Integer)
    wind_type_speed = Column(String)
    wind_chill = Column(Integer)
    wind_unit = Column(String)
    local_timestamp = Column(String)



def timestamp2String(timestamp):
    import datetime
    return datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')



#Read file configuration
fname = "secret_forecast"
with open(fname) as f:
    content = f.readlines()

#TODO  get content correctly (via dict)
key = content[0].split(":")[1].rstrip().lstrip().strip()
secret = content[1].split(":")[1].rstrip().lstrip().strip()



#SQL alchemy
engine = create_engine('sqlite:///spots3.db')
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


#Defined spots
idBarceloneta = 3535





#API Reader
import requests

r = requests.get("http://magicseaweed.com/api/"+str(key)
        +"/forecast/?spot_id="+str(idBarceloneta)
        +"&units=eu"
        +"&fields=timestamp,localTimestamp,"
        +"fadedRating,solidRating,threeHourTimeText,"
        +"wind.*,condition.temperature,"
        +"charts.*")

json_values = r.json()


for value in json_values:
    #Parse times
    local_timestamp = value["localTimestamp"]
    solid_rating = value["solidRating"]
    faded_rating = value["fadedRating"]
    chart_wind_url =  value["charts"]["wind"]
    chart_period_url =  value["charts"]["period"]
   # chart_sst =  value["charts"]["sst"] #Honda
    wind_direction = value["wind"]["direction"]
    wind_compass_direction = value["wind"]["compassDirection"] #Brujula
    wind_speed = value["wind"]["speed"]
    wind_unit = value["wind"]["unit"]
    wind_chill = value["wind"]["chill"] #Frio
    #db_ins.execute()

    
    print "time: "+timestamp2String(local_timestamp)+" solidRating="+str(solid_rating)+" fadedRating="+str(faded_rating)
    print "chart_wind: "+str(chart_wind_url)
    print "chart_period: "+str(chart_period_url)
   # print "chart_sst: "+str(chart_sst)
    print "wind_direction: "+str(wind_direction)+" wind_compass_direction: "+wind_compass_direction
    print "wind_speed: "+str(wind_speed)+ " "+str(wind_unit)
    print "wind_chill: "+str(wind_chill)

    spot = InfoSpot(local_timestamp=local_timestamp,solid_rating=solid_rating,faded_rating=faded_rating
            ,chart_wind_url=chart_wind_url,chart_period_url=chart_period_url,wind_direction=wind_direction
            ,wind_compass_direction=wind_compass_direction, wind_unit=wind_unit
            ,wind_chill=wind_chill, wind_speed=wind_speed)

    session.add(spot)
    session.commit()



