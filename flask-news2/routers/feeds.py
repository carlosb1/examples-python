from fastapi import APIRouter
from pydantic import BaseModel
import logging
from typing import List
from db import get_collection
from bson import ObjectId

LOGGER = logging.getLogger("uvicorn")

import os
host_mongodb = os.getenv('HOST_MONGODB', '0.0.0.0')

# DTOs objects


class Feeds(BaseModel):
    feeds: List[str]


router = APIRouter()


@router.post('/feeds', status_code=201)
def addFeeds(feeds: Feeds):
    db = get_collection(host_mongodb, db_name="feeds")
    result_ids = []
    for feed in feeds.feeds:
        if not db.find_one({"url": feed}):
            LOGGER.info(str(feed))
            # TODO set up type
            new_id = db.insert_one({
                "url": feed,
                "status": "PENDING"
            }).inserted_id
            result_ids.append(str(new_id))
    return {"ids": result_ids}


@router.get('/feeds')
def getFeeds():
    feeds = get_collection(host_mongodb, db_name="feeds")
    feed_urls = [{
        "url": feed['url'],
        "item_id": str(feed['_id'])
    } for feed in feeds.find()]
    return {"feeds": feed_urls}


@router.delete('/feeds/{item_id}')
def deleteFeeds(item_id: str):
    db = get_collection(host_mongodb, db_name="feeds")
    db.delete_one({"_id": ObjectId(item_id)})
    return {"Result": "OK"}
