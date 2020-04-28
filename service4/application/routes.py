# import request & Response function from the flask module
import random
import requests

# import the app object from the ./application/__init__.py
from application import app

# define routes for /medium , this function will be called when these are accessed
@app.route('/generator', methods = ['GET','POST'])
def generator():
    colour_response = requests.get('http://service2:5001/colour')
    medium_response = requests.get('http://service3:5002/medium')
    random = colour_response.text + medium_response.text
    return random
