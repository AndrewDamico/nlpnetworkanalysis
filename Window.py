#!/usr/bin/env python
# 
# NLP 
# Andrew D'Amico
# MSDS 453 Natural Language Processing
# Northwestern University
# Copyright (c) 2022, Andrew D'Amico. All rights reserved.
# Licenced under BSD Licence.

import datetime
from NewsArticle import Corpus

class Window(object):
    """
    A Window is an object which contains pointers to a set of 
    news articles for a set window of time (days), starting
    from a specific date and working backwards.
    """
    
    def __init__(self, start_date: datetime.datetime = None, end_date: datetime.datetime = None,
                 lag: int = None, corpus: Corpus = None):
        self._start_date = start_date
        self._end_date = end_date
        self._lag = lag
        self._corpus = corpus
        self._curration = [x for x in self._corpus.corpus if self.start_date <= x.date and x.date <= self.end_date]
        self._articles = None
        self._titles = None
    
    @property
    def end_date(self):
        return self._end_date
    @property
    def start_date(self):
        if self._start_date == None:
            self._start_date = self.end_date - datetime.timedelta(self.lag)
        return self._start_date
    @property
    def lag(self):
        return self._lag
    @property
    def corpus(self):
        return self._curration
    @property
    def titles(self):
        if self._titles == None:
            self._titles = list(map(self.title_viewer, self.corpus))
        return self._titles
    @property
    def articles(self):
        if self._articles == None:
            self._articles = list(map(self.token_viewer, self.corpus))
        return self._articles
    @property
    def info(self):
        print (f'Start Date: {self.start_date}')
        print (f'End Date: {self.end_date}')
        print (f'lag: {self.lag}')
        print (f'Total Records: {len(self.corpus)}')
        return

    def token_viewer(self, entity):
        return entity.tokens

    def title_viewer(self, entity):
        return entity.headline
