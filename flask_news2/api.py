from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from redis import Redis
from rq import Queue
import logging

from worker import runTask

LOGGER = logging.getLogger()

app = FastAPI()

redis_conn = Redis(host='redis', port=6379, db=0)
q = Queue('my_queue', connection=redis_conn)


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
