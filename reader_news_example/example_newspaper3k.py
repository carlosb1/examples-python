from newspaper import  Article
import asyncio

list_articles_to_analyse = ["http://www.lavanguardia.com/local/girona/20171108/432719485798/miles-personas-cortan-via-ave-girona.html"]


class RepositoryArticle:
    def __init__(self):
        self.info  = []
    def add_article(self,publish_date,title,text,  article, link_image, link_videos, keywords):
        self.info.append([publish_date,title,text,  article, link_image, link_videos, keywords])


async def download_article(url, repository_articles):
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
    repository_articles.add_article(publish_date, title, text, article, link_image, videos, keywords)

#TODO apply asyncio

loop = asyncio.get_event_loop()
repository=RepositoryArticle()
for url_article in list_articles_to_analyse:
    loop.run_until_complete(download_article(url_article,repository))
print(str(repository.info))
loop.close()
