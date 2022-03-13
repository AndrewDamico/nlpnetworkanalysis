#!/usr/bin/env python
#
# NLP Language Network Analysis
# Andrew D'Amico
# MSDS 453 Natural Language Processing
# Northwestern University
# Copyright (c) 2022, Andrew D'Amico. All rights reserved.
# Licenced under BSD Licence.

import os
import pandas as pd
import glob
import re, string
from nltk.corpus import stopwords

def tokenization(doc):
    #split document into individual words
    tokens=doc.split()
    re_punc = re.compile('[%s]' % re.escape(string.punctuation))
    # remove punctuation from each word
    tokens = [re_punc.sub('', w) for w in tokens]
    # remove remaining tokens that are not alphabetic
    tokens = [word for word in tokens if word.isalpha()]
    # filter out short tokens
    tokens = [word for word in tokens if len(word) > 4]
    #lowercase all words
    tokens = [word.lower() for word in tokens]
    # filter out stop words
    stop_words = set(stopwords.words('english'))
    tokens = [w for w in tokens if not w in stop_words]
    # word stemming
    # ps=PorterStemmer()
    # tokens=[ps.stem(word) for word in tokens]
    return tokens

def One_Hot(variable):
    LE=LabelEncoder()
    LE.fit(variable)
    Label1=LE.transform(variable)
    OHE=OneHotEncoder()
    labels=OHE.fit_transform(Label1.reshape(-1,1)).toarray()
    return labels, LE, OHE

def newsloader(records: list = ["*.csv"], directory='headlines'):

    path = os.getcwd()
    working_dir = os.path.join(path, directory)
    csv_files = []
    
    for i in records:
        csv_files.extend(glob.glob(os.path.join(working_dir, i)))
        
    news = pd.DataFrame()
    
    for file in csv_files:
        df = pd.read_csv(file)
        news = pd.concat([news,df], ignore_index=True)
        
    print (f'Total files: {len(records)}')
    print (f'Total records: {len(news)}')
    
    return news
    
