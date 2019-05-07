from fastapi import APIRouter
from pydantic import BaseModel
from redis import Redis
from rq import Queue
import logging
from typing import List
from db import get_collection
from routers.ai import runAnalysis

LOGGER = logging.getLogger("uvicorn")

import os
host_redis = os.getenv('HOST_REDIS', 'redis')
host_mongodb = os.getenv('HOST_MONGODB', '0.0.0.0')

# Configure queue
redis_conn = Redis(host=host_redis, port=6379, db=0)
q = Queue('my_queue', connection=redis_conn)

# DTOs objects


class Links(BaseModel):
    elems: List[str]


class Tags(BaseModel):
    tags: List[str]


router = APIRouter()


@router.post('/news', status_code=201)
def addNews(links: Links):
    for link in links.elems:
        LOGGER.info(str(link))
        q.enqueue(runAnalysis, link, host_mongodb)
    return {"job": "Ok"}


@router.get('/news')
def getNews():
    news = get_collection(host_mongodb)
    result = []
    for elem in news.find():
        new_elem = elem
        elem["elem_id"] = str(elem["_id"])
        del elem["_id"]
        result.append(new_elem)

    return {"result": result}


# TODO Add search tags parameters
# TODO Add elastic search


@router.get('/news/search')
def searchNews(tags: Tags):
    return {"Result": "OK"}
