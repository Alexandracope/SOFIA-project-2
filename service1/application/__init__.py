
from flask import Flask

from flask_mysqldb import MySQL

from os import getenv
 
app = Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_HOST'] = getenv('MYSQLHOST')
app.config['MYSQL_USER'] = getenv('MYSQLUSER')
app.config['MYSQL_DB'] = getenv('MYSQLDB')
app.config['MYSQL_PASSWORD'] = getenv('MYSQLPASSWORD')

from application import routes
