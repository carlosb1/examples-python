from pymongo import MongoClient
import logging
LOGGER = logging.getLogger()


def get_collection(host_mongodb):
    LOGGER.info("Get connection")
    connection = MongoClient(host_mongodb, 27017)
    db = connection['db_news']
    news = db['news']
    return news


def dict_from_class(cls, keys_to_analyse=[], included=False):
    return dict((key, value) for (key, value) in cls.__dict__.items()
                if ((key in keys_to_analyse) == included))


def runAnalysis(link: str, host_mongodb: str):
    news = get_collection(host_mongodb)
    if not news.find_one({'link': link}):
        news.insert_one({'link': link, "status": "PENDING"})
        # TODO Apply ray

    LOGGER.debug("Working with this link: " + link)
