from microblog.app import app
from flask import render_template, flash, redirect, url_for
from forms import LoginForm


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


@app.route('/login', methods=['GET', 'POST'])
def Login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign in', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
