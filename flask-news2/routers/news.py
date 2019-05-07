from fastapi import APIRouter
from pydantic import BaseModel
from redis import Redis
from rq import Queue
import logging
from typing import List

from routers.ai import runAnalysis

LOGGER = logging.getLogger("uvicorn")

import os
host_redis = os.getenv('HOST_REDIS', 'redis')
host_mongodb = os.getenv('HOST_MONGODB', '0.0.0.0')

# Configure queue
redis_conn = Redis(host=host_redis, port=6379, db=0)
q = Queue('my_queue', connection=redis_conn)


class Links(BaseModel):
    elems: List[str]


router = APIRouter()


@router.post('/news', status_code=201)
def addNews(links: Links):
    for link in links.elems:
        LOGGER.info(str(link))
        q.enqueue(runAnalysis, link, host_mongodb)
    return {"job": "Ok"}


@router.get('/news')
def getNews():
    from db import get_collection
    news = get_collection(host_mongodb)
    elems = [str(elem) for elem in news.find()]
    return {"result": elems}
