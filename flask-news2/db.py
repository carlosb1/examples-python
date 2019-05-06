from pymongo import MongoClient
import logging
LOGGER = logging.getLogger()


def get_collection(host_mongodb):
    LOGGER.info("Get connection")
    connection = MongoClient(host_mongodb, 27017)
    db = connection['db_news']
    news = db['news']
    return news