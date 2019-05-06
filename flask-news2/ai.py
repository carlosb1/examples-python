import logging
from db import get_collection

LOGGER = logging.getLogger()


def dict_from_class(cls, keys_to_analyse=[], included=False):
    return dict((key, value) for (key, value) in cls.__dict__.items()
                if ((key in keys_to_analyse) == included))


def runAnalysis(link: str, host_mongodb: str):
    news = get_collection(host_mongodb)
    if not news.find_one({'link': link}):
        news.insert_one({'link': link, "status": "PENDING"})
        # TODO Apply ray

    LOGGER.debug("Working with this link: " + link)
