from fastapi import APIRouter
from pydantic import BaseModel
import logging
from typing import List

LOGGER = logging.getLogger("uvicorn")

# Configure queue

# DTOs objects


class URLs(BaseModel):
    urls: List[str]


router = APIRouter()


@router.post('/urls', status_code=201)
def addNews(urls: URLs):
    for url in urls.urls:
        LOGGER.info(str(url))
    return {"job": "Ok"}
