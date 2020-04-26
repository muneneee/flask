class Config:
    '''
    General config parent class
    '''
    pass


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