#!/usr/bin/env python
#
# NLP Language Network Analysis
# Andrew D'Amico
# MSDS 453 Natural Language Processing
# Northwestern University
# Copyright (c) 2022, Andrew D'Amico. All rights reserved.
# Licenced under BSD Licence.

import os
import time
import requests
import datetime
import dateutil
import pandas as pd
from dateutil.relativedelta import relativedelta

excluded_sections = ['Style', 'The Learning Network', 'Arts',
                     'Opinion', 'Books', 'Corrections', 'Food',
                     'T Magazine', 'Times Insider', 'Magazine',
                     'The Upshot', 'Crosswords & Games', 'Reader Center',
                     'Fashion & Style', 'Podcasts', 'Sports', 'Theater',
                     'Parenting', 'Movies']

excluded_news = ['Podcasts', 'Summary']

def get_nyt_articles(n=1):
    '''
    get_nyt_articles() takes a date or a range of dates and returns csv
    files listing all of the news headlines, by month.

    Keyword Arguments:

    start_date -- first date to retrieve
    end_date -- last date to retrieve
    n -- number of years to fetch
    '''

    end = datetime.date.today()
    start = end - relativedelta(years=n)

    #end = datetime.date(2020, 12, 31)
    #start = end - relativedelta(years=1)


    pd.date_range(start, end, freq='MS').strftime("%Y %m").tolist()

    months_in_range = [x.split(' ') for x in pd.date_range(
        start,
        end,
        freq='MS'
    ).strftime("%Y %#m").tolist()]


    def send_request(date):
        '''Sends a request to the NYT Archive API for given date.'''
        base_url = 'https://api.nytimes.com/svc/archive/v1/'
        url = base_url + '/' + date[0] + '/' + date[
            1] + '.json?api-key=' + 'IXgpV4G3MtKtTgzm7L54bXITJ2egifLm'
        response = requests.get(url).json()
        time.sleep(6)
        return response


    def is_valid(article, date):
        '''An article is only worth checking if it is in range, and has a headline.'''
        is_in_range = date > start and date < end
        has_headline = type(article['headline']) == dict and 'main' in article[
            'headline'].keys()
        return is_in_range and has_headline


    def parse_response(response):
        '''Parses and returns response as pandas data frame.'''
        data = {'headline': [],
                'date': [],
                'doc_type': [],
                'type_of_material': [],
                'snippet': [],
                'source': [],
                'news_desk': [],
                'section_name': [],
                'keywords': []}

        articles = response['response']['docs']
        optional_features = ['section_name', 'type_of_material', 'snippet',
                             'source', 'news_desk']

        for article in articles:  # For each article, make sure it falls within our date range
            date = dateutil.parser.parse(article['pub_date']).date()
            keywords = [keyword['value'] for keyword in article['keywords'] if
                        keyword['name'] == 'subject']
            if is_valid(article, date):
                data['date'].append(date)
                data['headline'].append(article['headline']['main'])
                data['doc_type'].append(article['document_type'])
                data['keywords'].append(keywords)
                for feature in optional_features:
                    if feature in article:
                        data[feature].append(article[feature])
                    else:
                        data[feature].append(None)

        return pd.DataFrame(data)

    def get_data(dates):
        '''Sends and parses request/response to/from NYT Archive API for given dates.'''
        total = 0
        print('Date range: ' + str(dates[0]) + ' to ' + str(dates[-1]))
        if not os.path.exists('headlines'):
            os.mkdir('headlines')
        for date in dates:
            response = send_request(date)
            df = parse_response(response)
            df_sorted = df[
                (df['doc_type'] == 'article') & (df['type_of_material'] == 'News')]
            df_sorted = df_sorted[
                ~df_sorted['section_name'].isin(excluded_sections)]
            df_sorted = df_sorted[~df_sorted['news_desk'].isin(excluded_news)]
            total += len(df_sorted)
            df_sorted.to_csv('headlines/' + date[0] + '-' + date[1] + '.csv',
                             index=False)
            print('Saving headlines/' + date[0] + '-' + date[1] + '.csv...')
        print('Number of articles collected: ' + str(total))


    get_data(months_in_range)
    return
