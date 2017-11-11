import urllib2
import sqlite3
import newspaper

class RepositoryArticle:
    def __init__(self):
        self.info  = []
    def add_article(self,publish_date,title,text,  article, link_image, link_videos, keywords):
        self.info.append([publish_date,title,text,  article, link_image, link_videos, keywords])


def save_info(database, url):
    article = Article(url)
    article.download()
    article.parse()
    publish_date = article.publish_date
    text = article.text
    link_image = article.top_image
    keywords = article.keywords
    videos = article.movies
    summary = article.summary
    title = article.title
    database.add_article(publish_date, title, text, article, link_image, videos, keywords)   


articles = RepositoryArticle()
PATH_DB='test.db'
conn = sqlite3.connect(PATH_DB)
cu = conn.cursor()
for row in cu.execute('SELECT * from news'):
    save_info(articles,row[1])
conn.close()

print articles.info

