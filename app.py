from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Database helper
def get_db_connection():
    conn = sqlite3.connect('database/phishing.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return "Welcome to Ethical Phishing Simulation Platform!"

if __name__ == '__main__':
    app.run(debug=True)

/create_campaign

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database/phishing.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_campaign', methods=['GET', 'POST'])
def create_campaign():
    if request.method == 'POST':
        name = request.form['name']
        template = request.form['template']

        conn = get_db_connection()
        conn.execute('INSERT INTO campaigns (name, template) VALUES (?, ?)', (name, template))
        conn.commit()
        conn.close()

        return "Campaign created successfully! Go back to <a href='/'>home</a>."

    return render_template('create_campaign.html')

if __name__ == '__main__':
    app.run(debug=True)
