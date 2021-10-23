from flask_login.utils import login_user
from .auth import get_valid_user, get_valid_registration, register_user
from .app import app
from flask import request, render_template, redirect, url_for
from flask_login import login_required, logout_user, current_user


@app.route('/')
@app.route('/home')
@login_required
def home():
    return render_template('home.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        user = get_valid_user(request.form)
        if user:
            login_user(user)
            return redirect(url_for('home'))   
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        registration = get_valid_registration(request.form)
        if registration:
            register_user(registration)
            return redirect(url_for('home'))
    return render_template('register.html')


@app.route('/chat')
@login_required
def chat():
    return render_template('chat.html')


@app.route('/rooms/<room_id>')
@login_required
def room(room_id):
    return render_template('room.html')
