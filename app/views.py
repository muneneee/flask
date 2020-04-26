from flask import render_template
from app import app

#views
@app.route('/')
def index():
    '''
    view page function that returns index page
    '''

    return render_template('index.html')