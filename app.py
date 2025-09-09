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
