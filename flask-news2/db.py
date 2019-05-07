from pymongo import MongoClient
import logging
LOGGER = logging.getLogger()


def get_collection(host_mongodb, table_name="news"):
    LOGGER.info("Get connection")
    connection = MongoClient(host_mongodb, 27017)
    db = connection['db_news']
    news = db[table_name]
    return news
