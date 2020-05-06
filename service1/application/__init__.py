from flask import Flask

from flask_mysqldb import MySQL

 
app = Flask(__name__)

mysql = MySQL(app)

app.config['MYSQL_HOST'] = ''
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''


from application import routes
