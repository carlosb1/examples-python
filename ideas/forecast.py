"""Docstring for MyClass."""

import datetime
import requests
from sqlalchemy import Column, Integer, String , create_engine
from celery import Celery
from sqlalchemy.sql import exists
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

# define object
class InfoSpot(Base):
    """Docstring for MyClass."""

    __tablename__ = 'infospot'
    id = Column(Integer, primary_key=True)
    solid_rating = Column(Integer)
    faded_rating = Column(Integer)
    chart_wind_url = Column(String)
    chart_period_url = Column(String)
    wind_direction = Column(Integer)
    wind_compass_direction = Column(String)
    wind_speed = Column(Integer)
    #wind_type_speed = Column(String)
    wind_chill = Column(Integer)
    wind_unit = Column(String)
    local_timestamp = Column(Integer)
    id_spot = Column(String)

    def __str__(self):
        """testing function."""
        result = 'id='+str(id)
        +' id_spot='+str(self.id_spot)
        +' solid_rating='+str(self.solid_rating)
        +' faded_rating='+str(self.faded_rating)
        +' chart_wind_url='+str(self.chart_wind_url)
        +' chart_period_url='+str(self.chart_period_url)
        +' wind_direction='+str(self.wind_direction)
        +' wind_compass_direction='+str(self.wind_compass_direction)
        +' wind_speed='+str(self.wind_speed)
        +' wind_chill='+str(self.wind_chill)
        +' wind_unit='+str(self.wind_unit)
        +' local_timestamp='+str(self.local_timestamp)

        return result

def timestamp_to_string(timestamp):
    """testing function."""
    return datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')


# API Reader
class ApiReader(object):
    """Docstring for MyClass."""

    def __init__(self, key, id_spot, session):
        """testing function."""
        self.id_spot = id_spot
        self.key = key
        self.url = 'http://magicseaweed.com/api/'+str(self.key)+'/forecast/?spot_id='+str(self.id_spot)+'&units=eu&fields=timestamp,localTimestamp,fadedRating,solidRating,threeHourTimeText,wind.*,condition.temperature,charts.*'
        self.session = session

    def update(self):
        """testing function."""
        r = requests.get(self.url)
        json_values = r.json()
        for value in json_values:
            #Parse times
            local_timestamp = value['localTimestamp']
            solid_rating = value['solidRating']
            faded_rating = value['fadedRating']
            chart_wind_url = value['charts']['wind']
            chart_period_url = value['charts']['period']
           # chart_sst =  value['charts']['sst'] #Honda
            wind_direction = value['wind']['direction']
            wind_compass_direction = value['wind']['compassDirection'] #Brujula
            wind_speed = value['wind']['speed']
            wind_unit = value['wind']['unit']
            wind_chill = value['wind']['chill'] #Frio
            print 'time: '+timestamp_to_string(local_timestamp)+' solidRating='+str(solid_rating)+' fadedRating='+str(faded_rating)
            print 'chart_wind: '+str(chart_wind_url)
            print 'chart_period: '+str(chart_period_url)
            print 'wind_direction: '+str(wind_direction)+' wind_compass_direction: '+wind_compass_direction
            print 'wind_speed: '+str(wind_speed)+' '+str(wind_unit)
            print 'wind_chill: '+str(wind_chill)
            spot = InfoSpot(solid_rating=solid_rating, faded_rating=faded_rating,
                    chart_wind_url=chart_wind_url, chart_period_url=chart_period_url,
                    wind_direction=wind_direction,
                    wind_compass_direction=wind_compass_direction,
                    wind_speed=wind_speed,
                    wind_chill=wind_chill,
                    wind_unit=wind_unit,
                    local_timestamp=local_timestamp,
                    id_spot=self.id_spot
                    )
            if not self.session.query(exists().where(InfoSpot.local_timestamp == local_timestamp).where(InfoSpot.id_spot == self.id_spot)).scalar():
                self.session.add(spot)
                self.session.commit()

#Read file configuration
fname = 'secret_forecast'
with open(fname) as f:
    content = f.readlines()

#TODO  get content correctly (via dict)
key = content[0].split(':')[1].rstrip().lstrip().strip()
secret = content[1].split(':')[1].rstrip().lstrip().strip()



#SQL alchemy
engine = create_engine('sqlite:///spots3.db')
Base.metadata.create_all(engine)


Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()



celery = Celery('forecast')
celery.config_from_object('celeryconfig')

#Defined spots
idBarceloneta = 3535
reader = ApiReader(key,idBarceloneta,session)


@celery.task
def search_spot():
    """testing function."""
    print 'Calling searching spot'
    reader.update()
