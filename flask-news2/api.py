from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

import logging

LOGGER = logging.getLogger("uvicorn")

import os
host_redis = os.getenv('HOST_REDIS', 'redis')
host_mongodb = os.getenv('HOST_MONGODB', '0.0.0.0')

app = FastAPI()

# CORS configuration
origins = ["*"]
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

from routers import news
app.include_router(news.router)
