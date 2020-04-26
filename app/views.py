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

    topheadlines = newsapi.get_top_headlines(sources="fox-news")

    articles = topheadlines['articles']

    desc = []
    news = []
    date = []
    link = []


    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        date.append(myarticles['publishedAt'])
        link.append(myarticles['url'])

    mylist = zip(news, desc, date,link)

    title = 'Home - Welcome to newshub'
    return render_template('index.html', title = title,context= mylist)



@app.route('/cnn')
def cnn():
    '''
    view page function that returns cnn page
    '''

    newsapi = NewsApiClient(api_key = 'e7f56e932284432c89095aa5928310c7' )

    topheadlines = newsapi.get_top_headlines(sources="cnn")

    articles = topheadlines['articles']

    desc = []
    news = []
    date = []
    link = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        date.append(myarticles['publishedAt'])
        link.append(myarticles['url'])

    mylist = zip(news, desc, date,link)

    title = 'Home - Welcome to newshub'
    return render_template('cnn.html', title = title,context= mylist)


@app.route('/espn')
def espn():
    '''
    view page function that returns espn page
    '''

    newsapi = NewsApiClient(api_key = 'e7f56e932284432c89095aa5928310c7' )

    topheadlines = newsapi.get_top_headlines(sources="espn")

    articles = topheadlines['articles']

    desc = []
    news = []
    date = []
    link = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        date.append(myarticles['publishedAt'])
        link.append(myarticles['url'])

    mylist = zip(news, desc, date,link)

    title = 'Home - Welcome to newshub'
    return render_template('espn.html', title = title,context= mylist)


@app.route('/fortune')
def fortune():
    '''
    view page function that returns fortune page
    '''

    newsapi = NewsApiClient(api_key = 'e7f56e932284432c89095aa5928310c7' )

    topheadlines = newsapi.get_top_headlines(sources="fortune")

    articles = topheadlines['articles']

    desc = []
    news = []
    date = []
    link =[]

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        date.append(myarticles['publishedAt'])
        link.append(myarticles['url'])

    mylist = zip(news, desc, date,link)

    title = 'Home - Welcome to newshub'
    return render_template('fortune.html', title = title,context= mylist)


@app.route('/ign')
def ign():
    '''
    view page function that returns ign page
    '''

    newsapi = NewsApiClient(api_key = 'e7f56e932284432c89095aa5928310c7' )

    topheadlines = newsapi.get_top_headlines(sources="ign")

    articles = topheadlines['articles']

    desc = []
    news = []
    date = []
    link = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        date.append(myarticles['publishedAt'])
        link.append(myarticles['url'])

    mylist = zip(news, desc, date,link)

    title = 'Home - Welcome to newshub'
    return render_template('ign.html', title = title,context= mylist)
