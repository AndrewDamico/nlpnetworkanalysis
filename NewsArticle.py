#!/usr/bin/env python
# 
# NLP 
# Andrew D'Amico
# MSDS 453 Natural Language Processing
# Northwestern University
# Copyright (c) 2022, Andrew D'Amico. All rights reserved.
# Licenced under BSD Licence.
import datetime
from NLPPrep import tokenization
import math

class NewsArticle(object):
    """
    A News Article is an object which contains a headline, a synopsis, 
    keywords, and meta data for processing.
    
    headline: Takes a string, generally in the form of a senten e
    date: string, in Y-m-day format
    synopsis: string
    keyword: list of keywords
    """
    def __init__(self, headline: str = None, date: str = None, synopsis: str = None, 
                 keywords: list =  None):
        self._headline = headline
        self._date = datetime.datetime.strptime(date, '%Y-%m-%d')
        self._synopsis = synopsis
        self._keywords = keywords
        self._tokens = None
        
    @property
    def headline(self):
        return self._headline
    @property
    def date(self):
        return self._date
    @property
    def synopsis(self):
        return self._synopsis
    @property
    def keywords(self):
        return self._keywords
    @property
    def tokens(self):
        if self._tokens:
            pass
        else:
            self._tokens = self.build_tokens()
        return self._tokens

    def build_tokens(self):
        container = " "
        try:
             if self.headline:
                container = tokenization(self.headline)
                pass
        except:
            print ("Cant tokenize headline")
        try:
            if self.synopsis:
                container += tokenization(self.synopsis)
            else:
                pass
        except:
            if math.isnan(self.synopsis):
                self._synopsis = " "
            else:
                pass
        temp_DSI = container[0]
        for word in range(1, len(container)):
            temp_DSI += ' '+container[word]
            
        return temp_DSI

class Corpus(object):
    """
    A Corpus is a collection of News Articles of the class NewsArticles
    """
    def __init__(self, db = None):
        self._corpus = self.build_corpus(db, parser=NewsArticle)
        
    @property
    def corpus(self):
        return self._corpus
    
    def build_corpus(self, db, parser=NewsArticle):
        corpus = [(
            parser(
                headline=row.headline, 
                date=row.date,
                synopsis=row.snippet, 
                keywords=row.keywords
            )) for index, row in db.iterrows() 
        ]
        return corpus
