from flask import Flask, render_template, request, url_for, session
from flask_mysqldb import MySQL
from templates import *
from static import *

#initialize our flask app
app = Flask('__name__')
app.secret_key = 'Your-secret key'

#MySQL config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask_users'

mysql = MySQL(app)

#route trigger for home page
@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    else:
        return render_template('home.html')