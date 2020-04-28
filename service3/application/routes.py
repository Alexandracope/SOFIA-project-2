# import request & Response function from the flask module
import requests

# import the app object from the ./application/__init__.py
from application import app

import random

# define routes for /medium , this function will be called when these are accessed
@app.route('/medium', methods = ['GET'])
def medium():
    medium = ['Pencil', 'Acrylic Paint','Watercolour Paint','Crayons', 'Coloured Pencils', 'Newspaper']
    return medium[random.randrange(6)]

