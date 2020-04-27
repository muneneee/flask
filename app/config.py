import os

class Config:
    '''
    General config parent class
    '''
    NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    SOURCE_API_BASE_URL ='http://newsapi.org/v2/sources?country=gb&apiKey={}'


class Prodconfig(Config):
    '''
    production config child class
    '''
    pass


class DevConfig(Config):
    '''
    Development config child class
    '''


    DEBUG = True
