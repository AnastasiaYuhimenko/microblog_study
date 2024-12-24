from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Anastasia'}
    posts = [
        {'author': {'username': 'Vladik'}, 'body': 'Iˆm a goose'},
        dict(author={'username': 'Goose'}, body='Iˆm a Vladik')
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/test')
def test():
    return 'test app'


@app.route('/user/<string:name>/<int:id>')
def user_page(name, id):
    return render_template('user_page.html', title='userpage', name=name, id=id)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
