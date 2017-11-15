from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, exists
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, Unicode, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class News(Base):
    __tablename__='news'
    id = Column(Integer,primary_key=True)
    link = Column(Unicode, unique= True)
    received_date = Column(DateTime(), default=datetime.datetime.now)
    analysed_date = Column(DateTime())
    status = Column(Unicode)
    info = Column(Unicode)
    publish_date = Column(DateTime())
    text = Column(Unicode)
    link_image = Column(Unicode)
    keywords = Column(Unicode)
    videos  = Column(Unicode)
    summary = Column(Unicode)
    title = Column(Unicode)
