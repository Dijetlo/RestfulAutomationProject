from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    test_user = {'username': 'Administrator'}
    return render_template('index.html', title='RAP Project', user=test_user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user: { form.username.data}    Persistent: {form.remember_me.data}')
        return redirect(url_for('/index'))
    return render_template('login.html', title='Sign In ', form=form)
