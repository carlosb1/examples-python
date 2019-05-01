FROM python:3.6-alpine

RUN apk add --update make cmake gcc g++ gfortran

RUN adduser -D flask_news
WORKDIR /home/flask_news

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
COPY api.py ./
COPY worker.py ./

RUN chown -R flask_news:flask_news ./
USER flask_news

CMD uvicorn api:app --host 0.0.0.0 --port 5057

