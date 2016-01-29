#!/usr/bin/python
import requests
from requests.auth import AuthBase
import hmac
import hashlib
import time
from celery import Celery


#define object
class InfoSpot(object):
    def __init__(self,local_timestamp,solid_rating,faded_rating,chart_wind,chart_period,wind_direction,wind_compass_direction, wind_unit, wind_chill, wind_speed):
        self.local_timestamp = local_timestamp
        self.solid_rating = solid_rating
        self.faded_rating = faded_rating
        self.chart_wind = chart_wind
        self.chart_period = chart_period
        self.wind_direction = wind_direction
        self.wind_compass_direction = wind_compass_direction
        self.wind_unit = wind_unit
        self.wind_chill = wind_chill
        self.wind_speed = wind_speed



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
from sqlalchemy import *
db = create_engine('sqlite:///spots.db')
db.echo = False
metad MetaData(db)
#id
spots = Table('spots',metadata,
        Column('id_post',String(40)),
        Column('time',String(30)),
        Column('solid_rating',Integer),
        Column('faded_rating',Integer),
        Column('chart_wind_url',String),
        Column('chart_period_url',String),
        Column('wind_direction',Integer),
        Column('wind_compass_direction',String),
        Column('wind_speed',Integer),
        Column('wind_type_speed',String),
        Column('wind_chill',Integer)
        )
spots.create()
db_ins = spots.insert()


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
    chart_wind =  value["charts"]["wind"]
    chart_period =  value["charts"]["period"]
   # chart_sst =  value["charts"]["sst"] #Honda
    wind_direction = value["wind"]["direction"]
    wind_compass_direction = value["wind"]["compassDirection"] #Brujula
    wind_speed = value["wind"]["speed"]
    wind_unit = value["wind"]["unit"]
    wind_chill = value["wind"]["chill"] #Frio
    #db_ins.execute()

    
    print "time: "+timestamp2String(local_timestamp)+" solidRating="+str(solid_rating)+" fadedRating="+str(faded_rating)
    print "chart_wind: "+str(chart_wind)
    print "chart_period: "+str(chart_period)
   # print "chart_sst: "+str(chart_sst)
    print "wind_direction: "+str(wind_direction)+" wind_compass_direction: "+wind_compass_direction
    print "wind_speed: "+str(wind_speed)+ " "+str(wind_unit)
    print "wind_chill: "+str(wind_chill)



