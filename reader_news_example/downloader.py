import sqlite3
import newspaper
from newspaper import Article
from sqlalchemy import create_engine, exists
from sqlalchemy.orm import relationship, sessionmaker
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

import json
class RepositoryArticle:
    def __init__(self, session):
        self.info  = {}
        self.session = session
    def add_article(self,link, publish_date,title,text, link_image, link_videos, keywords):
        self.info[link] = [publish_date,title,text, link_image, link_videos, keywords]
    def commit_all(self):
        for key in self.info.keys():
            info = self.session.query(News).filter(News.link==key).one()
            info.status = 'PARSED'
            print(self.info[key][0])
            info.publish_date = self.info[key][0]
            info.title = self.info[key][1]
            info.text = self.info[key][2]
            info.link_image = json.dumps(self.info[key][3])
            info.link_videos = json.dumps(self.info[key][4])
            info.keywords= json.dumps(self.info[key][5])
            self.session.flush()
            self.session.commit()


def save_info(database, url):
    article = Article(url)
    article.download()
    import time
    print("Sleeping...")
    time.sleep(10)
    print("slept")
    article.parse()
    publish_date = article.publish_date
    print("publish_date="+str(publish_date))
    text = article.text
    print("text="+str(text))
    link_image = article.top_image
    keywords = article.keywords
    videos = article.movies
    summary = article.summary
    title = article.title
    database.add_article(url,publish_date, title, text, link_image, videos, keywords)   


PATH_DB='test.db'

Session = sessionmaker()
engine = create_engine('sqlite:///'+PATH_DB)
Session.configure(bind=engine)
session = Session()

articles = RepositoryArticle(session)

news = session.query(News).all()
for new in news:
    save_info(articles,new.link)

articles.commit_all()

