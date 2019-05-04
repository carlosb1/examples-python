from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from redis import Redis
from rq import Queue
from pymongo import MongoClient

import logging
from typing import List

from worker import runTask
from ai import runAnalysis

LOGGER = logging.getLogger("uvicorn")

import os
host_redis = os.getenv('HOST_REDIS', 'redis')
host_mongodb = os.getenv('HOST_MONGODB', '0.0.0.0')


app = FastAPI()

# CORS configuration
origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# Configure queue
redis_conn = Redis(host=host_redis, port=6379, db=0)
q = Queue('my_queue', connection=redis_conn)

# DATABASE


def get_collection():
    connection = MongoClient(host_mongodb, 27017)
    db = connection['db_news']
    news = db['news']
    return news

# DTO instances


class Links(BaseModel):
    elems: List[str]

# TODO option to add tags


@app.post('/news', status_code=201)
def addNews(links: Links):
    for link in links.elems:
        LOGGER.info(str(link))
        q.enqueue(runAnalysis, link, get_collection())
    return {"job": "Ok"}


# test services

class Group(BaseModel):
    owner: str
    description: str = None


@app.get('/hello')
def hello():
    return {'hello': 'world'}


@app.post('/groups/{group_name}', status_code=201)
def addTask(group_name: str, group: Group):
    if group_name not in ('group1', 'group2'):
        raise HTTPException(status_code=404, detail='Group not found')
    q.enqueue(runTask, group_name, group.owner, group.description)
    return {'job': "Ok"}
