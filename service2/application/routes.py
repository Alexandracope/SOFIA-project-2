from application import app
import random
import requests

@app.route('/colour', methods=['GET'])
def colour():
    #An array of colours
    listofcolours = ['Red', 'Yellow', 'Pink', 'Blue', 'Orange', 'Purple', 'Green']
    #Random colour from the array of colours is chosen 
    return listofcolours[random.randrange(7)]
