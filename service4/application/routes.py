# import request & Response function from the flask module
from flask import request, Response

# import the app object from the ./application/__init__.py
from application import app

# define routes for /medium , this function will be called when these are accessed
@app.route('/generator', methods = ['GET'])
def generator():
    color = request.get('http://Service2:5001/color')
    medium = request.get('http://service3:5002/medium')
    return Response(color, medium, mimetype='text/plain')

