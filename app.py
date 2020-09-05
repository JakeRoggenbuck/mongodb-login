from flask import Flask, render_template, request, session, flash, redirect, url_for
import os
import database


app = Flask(__name__)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')


@app.route('/login', methods=['POST'])
def do_admin_login():
    username = request.form['username']
    password = request.form['password']
    if database.not_empty_login(username, password):
        if database.check_password(username, password):
            return render_template('secret_page.html', username=username)
        return "Ahhh"
    return render_template('login.html')


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4000)
