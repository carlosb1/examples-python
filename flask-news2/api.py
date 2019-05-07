from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS configuration
origins = ["*"]
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

from routers import news, urls, feeds
app.include_router(news.router)
app.include_router(urls.router)
app.include_router(feeds.router)
