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
    USERNAME = request.form['username']
    PASSWORD = request.form['password']
    DATABASE = database.Database()
    if DATABASE.not_empty_login(USERNAME, PASSWORD):
        if DATABASE.check_password(USERNAME, PASSWORD):
            return render_template('secret_page.html', username=USERNAME)
        return "Ahhh"
    return render_template('login.html')


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4000)
