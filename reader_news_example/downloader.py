import sqlite3
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, exists

import newspaper
from newspaper import Article
from news import News

import json
import asyncio

@asyncio.coroutine
def save_info(session, url):
    article = Article(url)
    article.download()
    import time
    time.sleep(10)
    article.parse()
    publish_date = article.publish_date
    text = article.text
    link_image = article.top_image
    keywords = article.keywords
    videos = article.movies
    summary = article.summary
    title = article.title
    print("summary="+summary)

    info = session.query(News).filter(News.link==url).one()
    info.status = 'PARSED'
    info.publish_date = publish_date
    info.title = title
    info.text = text
    info.summary = summary
    info.link_image = json.dumps(link_image)
    info.link_videos = json.dumps(videos)
    info.keywords= json.dumps(keywords)
    session.flush()
    session.commit()


def update(database_name='sqlite:///test.db'):
    
    Session = sessionmaker()
    engine = create_engine(database_name)
    Session.configure(bind=engine)
    session = Session()
    news = session.query(News).all()

    loop = asyncio.get_event_loop()
    tasks = []
    for new in news:
        tasks.append(save_info(session,new.link))
    
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

update()
