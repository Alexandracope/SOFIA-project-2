from flask import Flask

from flask_mysqldb import MySQL

from os import getenv
 
app = Flask(__name__)
# mysql = MySQL(app)

# app.config['MYSQL_HOST'] = getenv('MYSQL_HOST')
# app.config['MYSQL_USER'] = getenv('MYSQL_USER')
# app.config['MYSQL_PASSWORD'] = getenv('MYSQL_PASSWORD')
# app.config['MYSQL_DB'] = getenv('MYSQL_DB')
# app.config['MYSQL_PORT'] = getenv('MYSQLPORT')
# app.config['MYSQL_UNIX_SOCKET'] = getenv('MYSQL_SOCKET')

# cnx = mysql.connector.connect(user="carftdb@carftdb", password={getenv('MYSQL_PASSWORD')}, host="carftdb.mysql.database.azure.com", port=3306, database={craftdb}, ssl_ca={ca-cert filename}, ssl_verify_cert=true)

# cnx = mysql.connector.connect(user=getenv('MYSQLUSER'), password=getenv('MYSQLPASSWORD'), database=getenv('MYSQLDB'))

from application import routes
