from flask import render_template
from app import app

#views
@app.route('/')
def index():
    '''
    view page function that returns index page
    '''

    title = 'Home - Welcome to newshub'
    return render_template('index.html', title = title)


@app.route('/news/<int:news_id>')
def news(news_id):
    '''
    view more to read more on article
    '''
    return render_template('news.html',id = news_id)