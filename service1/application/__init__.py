
from flask import Flask

from flask_mysqldb import MySQL

from os import getenv

 
app = Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_HOST'] = ''
app.config['MYSQL_USER'] = ''
app.config['MYSQL_DB'] = ''
app.config['MYSQL_PASSWORD'] = ''

from application import routes
