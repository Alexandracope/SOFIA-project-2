from application import app
import random
import requests

@app.route('/colour', methods=['GET'])
def colour():

    listofcolours = ['Red', 'Yellow', 'Pink', 'Blue', 'Orange', 'Purple', 'Green']

    return listofcolours[random.randrange(7)]
