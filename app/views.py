from flask import render_template
from app import app
from .request import get_news
from newsapi import NewsApiClient

#views
@app.route('/')
def index():
    '''
    view page function that returns index page
    '''

    newsapi = NewsApiClient(api_key = 'e7f56e932284432c89095aa5928310c7' )

    topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english")

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img)

    title = 'Home - Welcome to newshub'
    return render_template('index.html', title = title,context= mylist)


@app.route('/news/<int:news_id>')
def news(news_id):
    '''
    view more to read more on article
    '''
    return render_template('news.html',id = news_id)