from flask_login.utils import login_user
from .auth import get_valid_user
from .app import app, db, load_user
from .user import User
from flask import request, render_template, redirect, url_for
from flask_login import login_required, current_user, logout_user


@app.route('/')
@app.route('/home')
@login_required
def index():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        user = get_valid_user(request.form, db)
        if user:
            login_user(user)
            return redirect(url_for('index'))   
    return render_template('login.html')


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        # do stuff
        pass
    return render_template('register.html')