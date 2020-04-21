# import request & Response function from the flask module
from flask import request, Response
import requests

# import the app object from the ./application/__init__.py
from application import app

from random import randint

# define routes for /medium , this function will be called when these are accessed
@app.route('/medium', methods = ['GET'])
def medium():
    medium = ['Pencil', 'Acrylic Paint','Watercolour Paint','Crayons', 'Coloured Pencils', 'Newspaper']
    return Response(medium[randint(0,5)], mimetype='text/plain')

