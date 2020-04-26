from app import app
import urllib.request,json
from .models import source
from .models import news

Source = source.Source
News = news.News

#getting api key
apikey = app.config['NEWS_API_KEY']

#getting source base url
base_url = app.config["SOURCE_API_BASE_URL"]



def get_sources():
    '''
    gets the json response to url request
    '''
    get_sources_url = base_url.format(apikey)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_sources = None

        if get_sources_response['sources']:
            source_sources_list = get_sources_response['sources']
            source_sources = process_sources(source_sources_list)

    return source_sources