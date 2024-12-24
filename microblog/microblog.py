from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Настя'}
    posts = [
        {'author': {'username': 'Vladik'}, 'body':'Iˆm a goose'},
        dict(author={'username': 'Goose'}, body='Iˆm a Vladik')
    ]
    return render_template('index.html', title='Home',  user=user, posts=posts)
@app.route('/test')
def test():
    return 'test app'

if __name__ == '__main__':
    app.run()
