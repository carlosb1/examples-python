from pymongo import MongoClient
import logging
LOGGER = logging.getLogger()


def get_collection(host_mongodb, db_name="news"):
    LOGGER.info("Get connection")
    connection = MongoClient(host_mongodb, 27017)
    db = connection['db_news']
    news = db[db_name]
    return news
