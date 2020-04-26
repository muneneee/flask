from flask import render_template
from app import app

#views
@app.route('/')
def index():
    '''
    view page function that returns index page
    '''

    message = 'NEWSHUB'
    return render_template('index.html', message = message)


@app.route('/news/<int:news_id>')
def news(news_id):
    '''
    view more to read more on article
    '''
    return render_template('news.html',id = news_id)