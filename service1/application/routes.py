from flask import render_template
from application import app, mysql
from flask_mysqldb import MySQL
import requests



@app.route('/')
@app.route('/home', methods=['GET' , 'POST'])
def home():
    # response = requests.get('URL')
    response = requests.get('http://service4:5003/generator')
    random = response.text
    # Mysql commands used to insert result of get request to database table
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO result(result)VALUES(%s)", [random])
    mysql.connection.commit()
    cur.close()
    return render_template('home.html',random=random, title='Home')
