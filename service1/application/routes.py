from flask import render_template
from application import app
import requests

@app.route('/')
@app.route('/home', methods=['GET'])
def home():
    # response = requests.get('URL')
    response = requests.get('http://service4:5003/generator')
    random = response.text
    # print (random)
    return render_template('home.html',random=random, title='Home')
