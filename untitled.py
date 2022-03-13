#!/usr/bin/env python
# 
# NLP 
# Andrew D'Amico
# MSDS 453 Natural Language Processing
# Northwestern University
# Copyright (c) 2022, Andrew D'Amico. All rights reserved.
# Licenced under BSD Licence.
from datetime import datetime

class Window(object):
    """
    A Window is an object which contains pointers to a set of 
    news articles for a set window of time (days), starting
    from a specific date and working backwards.
    """
    
    def __init__(self, start_date: str = None, end_date: str = None,
                 lag: int = None, corpus: list = None):
        self._start_date = start_date
        self._end_date = end_date
        self._lag = lag
        self._corpus = corpus
    
    @property
    def end_date(self):
        if type(self._end_date) == datetime:
            
        return self._end_date
    @property
    def start_date(self):
        return self._start_date

    @property
    def lag(self):
        return self._lag
    @property
    def corpus(self):
        return self._corpus
    @property
    def titles(self):
    @property
    def articles(self):



------------------------------
        
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