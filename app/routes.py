from app import app
from flask import render_template
from datetime import datetime
from app.models import Post

@app.route('/')
def home():
    context = {
        'first_name': 'Derek',
        'last_name': 'Hawkins',
        'email': 'derekhcodingtemple.com',
        'posts': Post.query.all()
        # 'posts': [
        #     {
        #         'id': 1,
        #         'body': 'This is the first blog post',
        #         'date_created': datetime.utcnow()
        #     },
        #     {
        #         'id': 2,
        #         'body': 'This is the second blog post',
        #         'date_created': datetime.utcnow()
        #     },
        #     {
        #         'id': 3,
        #         'body': 'This is the third blog post',
        #         'date_created': datetime.utcnow()
        #     },
        # ]
    }
    return render_template('index.html', **context)

@app.route('/about')
def about():
    # data = {
    #     'first_name': 'Lucas',
    #     'last_name': 'Lang'
    # }
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/register')
def register():
    return render_template('register.html')