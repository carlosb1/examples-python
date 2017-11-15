import scipy
import numpy as np
import pandas as pd
import nltk
import re
import os
import codecs
from sklearn import feature_extraction
import mpld3

from news import News
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, exists
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, exists


Session = sessionmaker()
engine = create_engine('sqlite:///test.db')
Session.configure(bind=engine)
session = Session()
news = session.query(News).all()
links = []
titles = []
texts = []
for new in news:
    links.append(new.link)
    titles.append(new.title)
    texts.append(new.text)


def tokenize_and_stem(text):
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenizer(sent)]
    filtered_tokens = []

    for token in tokens:
        if re.search('[a-zA-Z]',token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems

def tokenize_only(text):
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []

    for token in tokens:
        if re.search('[a-zA-Z]',token):
            filtered_tokens.append(token)
    return filtered_tokens

totalvocab_stemmed = []
totalvocab_tokenized = []

for i in synopses:
    allwords_stemmed = tokenize_and_stem(i)
    totalvocab_stemmed.extend(allwords_stemmed)

    allwords_tokenized = tokenize_only(i)
    totalvocab_tokenized,extend(allwords_tokenized)



nltk.download('stopwords')

stopwords = nltk.corpus.stopwords.words('spanish')

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer('spanish')


