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
summaries = []
for new in news:
    links.append(new.link)
    titles.append(new.title)
    texts.append(new.text)
    summaries.append(new.summary)


def tokenize_and_stem(text):
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
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




nltk.download('stopwords')
nltk.download('punkt')

stopwords = nltk.corpus.stopwords.words('spanish')

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer('spanish')


totalvocab_stemmed = []
totalvocab_tokenized = []

for i in texts:
    allwords_stemmed = tokenize_and_stem(i)
    totalvocab_stemmed.extend(allwords_stemmed)

    allwords_tokenized = tokenize_only(i)
    totalvocab_tokenized.extend(allwords_tokenized)


vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index=totalvocab_stemmed)
print 'there are '+str(vocab_frame.shape[0]) + ' items in vocab_frame'
print vocab_frame.head()


#Apply tfid vectorization
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=200000, min_df=0.2, stop_words=None, use_idf=True, tokenizer=tokenize_and_stem, ngram_range=(1,3))

tfidf_matrix = tfidf_vectorizer.fit_transform(texts)

print tfidf_matrix.shape


terms = tfidf_vectorizer.get_feature_names()


from sklearn.metrics.pairwise import cosine_similarity
dist = 1 - cosine_similarity(tfidf_matrix)


from sklearn.cluster import KMeans
num_clusters = 5
km = KMeans(n_clusters = num_clusters)
km.fit(tfidf_matrix)
clusters = km.labels_.tolist()

from sklearn.externals import joblib
#km = joblib.load('doc_cluster.pkl')


