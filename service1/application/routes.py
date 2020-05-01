from flask import render_template
from application import app
import requests

@app.route('/')
@app.route('/home', methods=['GET' , 'POST'])
def home():
    # response = requests.get('URL')
    response = requests.get('http://service4:5003/generator')
    random = response.text
    
    # print (random)
    
    # 6209a358e24e918980493bb7749ae3f2be5545a9
    return render_template('home.html',random=random, title='Home')
