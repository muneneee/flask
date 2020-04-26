from app import app
import urllib.request,json
from .models import source
from .models import news

Source = source.Source
News = news.News

#getting api key
apiKey = app.config['NEWS_API_KEY']

#getting source base url
base_url = app.config['NEWS_API_BASE_URL']




def get_news(country):
    '''
    gets the json response to url request
    '''
    get_news_url = base_url.format(country,apiKey)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        new_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)

    return news_results



def process_results(news_list):
    '''
    transform news into objects
    '''

    news_results = []
    for news_item in news_list:
        name = news_item.get('name')
        description = news_item.get('description')

    return news_results